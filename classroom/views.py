from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, OnlineSession, Assignment, AssignmentSubmission, ClassStudent
from accounts.models import Teacher, Student, User
from .services import ClassroomService
import logging

logger = logging.getLogger(__name__)

classroom_service = ClassroomService()

def teacher_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'teacher':
        return redirect('accounts:login')

    teacher = get_object_or_404(Teacher, user=request.user)
    classes = Classes.objects.filter(teacher=teacher)
    sessions = OnlineSession.objects.filter(teacher=teacher).order_by('-start_time')
    assignments = Assignment.objects.filter(teacher=teacher).order_by('-created_at')

    return render(request, 'classroom/teacher_dashboard.html', {
        'classes': classes,
        'sessions': sessions,
        'assignments': assignments
    })

def developer_dashboard(request):
    if not request.user.is_authenticated or request.user.role not in ['admin', 'developer']:
        return redirect('accounts:login')

    students = Student.objects.all().select_related('user')
    teachers = Teacher.objects.all().select_related('user')
    classes = Classes.objects.all()

    return render(request, 'classroom/developer_dashboard.html', {
        'students': students,
        'teachers': teachers,
        'classes': classes
    })

def create_online_session(request):
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.role != 'teacher':
            return redirect('accounts:login')

        classroom_service.create_online_session(
            teacher_user=request.user,
            class_id=request.POST.get('class_id'),
            topic=request.POST.get('topic'),
            start_time=request.POST.get('start_time'),
            duration=request.POST.get('duration')
        )
        return redirect('classroom:teacher_dashboard')
    return redirect('classroom:teacher_dashboard')

def delete_user(request, user_id):
    if not request.user.is_authenticated or request.user.role not in ['admin', 'developer']:
        return redirect('accounts:login')

    user = get_object_or_404(User, user_id=user_id)
    user.delete()
    return redirect('classroom:developer_dashboard')

def create_assignment(request):
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.role != 'teacher':
            return redirect('accounts:login')

        classroom_service.create_assignment(
            teacher_user=request.user,
            class_id=request.POST.get('class_id'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            due_date=request.POST.get('due_date'),
            attachments=request.FILES.getlist('attachments')
        )
        return redirect('classroom:teacher_dashboard')
    return redirect('classroom:teacher_dashboard')

def student_assignments(request):
    if not request.user.is_authenticated or request.user.role != 'student':
        return redirect('accounts:login')

    student = get_object_or_404(Student, user=request.user)
    class_ids = ClassStudent.objects.filter(student=student).values_list('classes_id', flat=True)
    assignments = Assignment.objects.filter(class_info_id__in=class_ids).order_by('-due_date')

    return render(request, 'classroom/student_assignments.html', {'assignments': assignments})

def submit_assignment(request, assignment_id):
    if request.method == 'POST':
        classroom_service.submit_assignment(
            student_user=request.user,
            assignment_id=assignment_id,
            content=request.POST.get('content'),
            file=request.FILES.get('submission_file')
        )
        return redirect('classroom:student_assignments')
    return redirect('classroom:student_assignments')

def grade_submission(request, submission_id):
    if request.method == 'POST':
        if request.user.role != 'teacher': return redirect('accounts:login')

        classroom_service.grade_submission(
            teacher_user=request.user,
            submission_id=submission_id,
            grade=request.POST.get('grade'),
            comment=request.POST.get('comment')
        )
        return redirect('classroom:teacher_dashboard')
    return redirect('classroom:teacher_dashboard')

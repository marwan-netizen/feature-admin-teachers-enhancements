from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Test, Result
from accounts.models import Student
from .services import TestingService
import logging

logger = logging.getLogger(__name__)

testing_service = TestingService()

def get_student_id(request):
    if not request.user.is_authenticated: return None
    student = Student.objects.filter(user=request.user).first()
    return student.student_id if student else None

def test_instructions(request):
    return render(request, 'testing/instructions.html')

def start_ai(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if testing_service.start_dynamic_test_session(request.session):
        return redirect('testing:reading_start')

    request.session['dynamic_tests_ready'] = False
    return redirect('testing:reading_start')

# Reading
def reading_start(request):
    return redirect('testing:reading_q1')

def reading_q1(request):
    test_id = request.session.get('dynamic_test_ids', {}).get('reading')
    if test_id:
        test = get_object_or_404(Test, test_id=test_id)
        questions = test.questions.prefetch_related('options').all()
        return render(request, 'testing/reading_q1.html', {'test': test, 'questions': questions})
    return render(request, 'testing/reading_q1.html')

def submit_reading(request, q):
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        test_id = request.session.get('dynamic_test_ids', {}).get('reading')
        if not test_id:
            test = Test.objects.filter(skill='reading').first()
            if not test: return redirect('testing:reading_done')
            test_id = test.test_id

        testing_service.process_mcq_submission(request.user, test_id, student_id, request.POST, 'reading')
        return redirect('testing:reading_done')
    return redirect('testing:reading_done')

def reading_done(request):
    return render(request, 'testing/reading_done.html')

# Listening
def listening_start(request):
    test_id = request.session.get('dynamic_test_ids', {}).get('listening')
    if test_id:
        test = get_object_or_404(Test, test_id=test_id)
        questions = test.questions.prefetch_related('options').all()
        return render(request, 'testing/listening_q1.html', {'test': test, 'questions': questions})
    return render(request, 'testing/listening_q1.html')

def submit_listening(request, q):
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        test_id = request.session.get('dynamic_test_ids', {}).get('listening')
        if not test_id:
            test = Test.objects.filter(skill='listening').first()
            if not test: return redirect('testing:listening_done')
            test_id = test.test_id

        testing_service.process_mcq_submission(request.user, test_id, student_id, request.POST, 'listening')
        return redirect('testing:listening_done')
    return redirect('testing:listening_done')

def listening_done(request):
    return render(request, 'testing/listening_done.html')

# Writing
def writing_start(request):
    test_id = request.session.get('dynamic_test_ids', {}).get('writing')
    if test_id:
        test = get_object_or_404(Test, test_id=test_id)
        return render(request, 'testing/writing_q1.html', {'test': test})
    return render(request, 'testing/writing_q1.html')

def submit_writing(request):
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        essay = request.POST.get('essay')
        test_id = request.session.get('dynamic_test_ids', {}).get('writing')
        if not test_id:
            test = Test.objects.filter(skill='writing').first()
            if not test: return redirect('testing:writing_done')
            test_id = test.test_id

        if essay:
            testing_service.process_writing_submission(request.user, test_id, student_id, essay)
        return redirect('testing:writing_done')

    return redirect('testing:writing_done')

def writing_done(request):
    return render(request, 'testing/writing_done.html')

# Speaking
def speaking_start(request):
    test_id = request.session.get('dynamic_test_ids', {}).get('speaking')
    if test_id:
        test = get_object_or_404(Test, test_id=test_id)
        return render(request, 'testing/speaking_q1.html', {'test': test})
    return render(request, 'testing/speaking_q1.html')

def submit_speaking(request):
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        transcription = request.POST.get('transcription', '')
        accuracy = int(request.POST.get('accuracy', 0))
        test_id = request.session.get('dynamic_test_ids', {}).get('speaking')

        if not test_id:
            test = Test.objects.filter(skill='speaking').first()
            if not test: return redirect('testing:speaking_done')
            test_id = test.test_id

        testing_service.process_speaking_submission(request.user, test_id, student_id, transcription, accuracy)
        return redirect('testing:speaking_done')
    return redirect('testing:results')

def speaking_done(request):
    return render(request, 'testing/speaking_done.html')

# Results
def results(request):
    results = Result.objects.filter(user=request.user).select_related('test')
    return render(request, 'testing/results.html', {'results': results})

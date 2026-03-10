"""
Database models for the Classroom module.

Defines the structure for classes, enrollments, assignments, submissions,
online sessions, and grades.
"""

from django.db import models
from accounts.models import User, Student, Teacher
from core.models import SoftDeleteModel

class Classes(SoftDeleteModel):
    """
    Represents a virtual class or course.
    """
    class_id = models.AutoField(primary_key=True)
    classes_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'classes'

class ClassStudent(models.Model):
    """
    Link table for student enrollment in classes.
    """
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'class_student'
        unique_together = ('classes', 'student')

class OnlineSession(SoftDeleteModel):
    """
    Represents a scheduled Jitsi video session.
    """
    session_id = models.AutoField(primary_key=True)
    class_info = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='class_id')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255, unique=True)
    topic = models.CharField(max_length=255)
    join_url = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=20, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'online_sessions'

class Assignment(SoftDeleteModel):
    """
    Represents a task assigned to students in a class.
    """
    class_info = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='class_id')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    max_grade = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assignments'

class AssignmentAttachment(SoftDeleteModel):
    """
    Represents a file attached to an assignment.
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='attachments')
    file_path = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assignment_attachments'

class AssignmentSubmission(SoftDeleteModel):
    """
    Represents a student's response to an assignment.
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    teacher_comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assignment_submissions'

class SubmissionVersion(SoftDeleteModel):
    """
    Represents a specific version of a student's submission.
    """
    submission = models.ForeignKey(AssignmentSubmission, on_delete=models.CASCADE, related_name='versions')
    content = models.TextField(null=True, blank=True)
    file_path = models.CharField(max_length=255, null=True, blank=True)
    version = models.IntegerField(default=1)
    is_late = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'submission_versions'

class Grade(SoftDeleteModel):
    """
    Consolidated grade records for students.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_info = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='class_id')
    midterm = models.IntegerField(null=True, blank=True)
    final = models.IntegerField(null=True, blank=True)
    oral = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'grades'

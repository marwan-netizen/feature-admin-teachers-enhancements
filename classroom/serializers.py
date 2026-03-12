from rest_framework import serializers
from .models import Classes, OnlineSession, Assignment, AssignmentSubmission, SubmissionVersion, Grade

class ClassSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.user.full_name', read_only=True)
    class Meta:
        model = Classes
        fields = ['class_id', 'classes_name', 'teacher', 'teacher_name', 'level', 'description']

class OnlineSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineSession
        fields = ['session_id', 'class_info', 'topic', 'room_name', 'join_url', 'start_time', 'duration', 'status']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'class_info', 'title', 'description', 'due_date', 'max_grade']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['id', 'assignment', 'student', 'status', 'grade', 'teacher_comment']

class GradeSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source='class_info.classes_name', read_only=True)
    class Meta:
        model = Grade
        fields = ['id', 'class_info', 'class_name', 'midterm', 'final', 'oral', 'notes']

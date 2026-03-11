from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Classes, ClassStudent, OnlineSession, Assignment, AssignmentAttachment, AssignmentSubmission, SubmissionVersion, Grade

@admin.register(Classes)
class ClassesAdmin(ModelAdmin):
    list_display = ("classes_name", "teacher", "level", "created_at")
    list_filter = ("level", "teacher")
    search_fields = ("classes_name", "description")

@admin.register(ClassStudent)
class ClassStudentAdmin(ModelAdmin):
    list_display = ("classes", "student", "created_at")
    list_select_related = ("classes", "student__user")

@admin.register(OnlineSession)
class OnlineSessionAdmin(ModelAdmin):
    list_display = ("topic", "class_info", "teacher", "start_time", "status")
    list_filter = ("status", "class_info")
    search_fields = ("topic", "room_name")

@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    list_display = ("title", "class_info", "teacher", "due_date")
    list_filter = ("class_info", "teacher")
    search_fields = ("title", "description")

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(ModelAdmin):
    list_display = ("assignment", "student", "status", "grade")
    list_filter = ("status", "assignment__class_info")
    list_select_related = ("assignment", "student__user")

@admin.register(Grade)
class GradeAdmin(ModelAdmin):
    list_display = ("user", "class_info", "midterm", "final", "oral")
    list_filter = ("class_info",)
    list_select_related = ("user", "class_info")

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ExerciseAttempt

@admin.register(ExerciseAttempt)
class ExerciseAttemptAdmin(ModelAdmin):
    list_display = ("user", "exercise_type", "score", "completed_at")
    list_filter = ("exercise_type", "completed_at")
    list_select_related = ("user",)

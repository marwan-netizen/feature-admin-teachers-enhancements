from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import LearningGap, TrainingPlan

@admin.register(LearningGap)
class LearningGapAdmin(ModelAdmin):
    list_display = ("user", "topic", "level", "detected_at", "resolved_at")
    list_filter = ("level", "detected_at", "resolved_at")
    list_select_related = ("user",)

@admin.register(TrainingPlan)
class TrainingPlanAdmin(ModelAdmin):
    list_display = ("user", "created_at", "is_active")
    list_filter = ("is_active",)
    list_select_related = ("user",)

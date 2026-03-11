from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ActivityLog, Notification

@admin.register(ActivityLog)
class ActivityLogAdmin(ModelAdmin):
    list_display = ("action", "user", "model_type", "model_id", "created_at")
    list_filter = ("action", "model_type", "created_at")
    search_fields = ("model_label", "user__email")
    list_select_related = ("user",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ("type", "notifiable_type", "read_at", "created_at")
    list_filter = ("type", "read_at")

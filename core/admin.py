from django.contrib import admin
from .models import ActivityLog, Notification

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'action', 'model_type', 'ip_address')
    list_filter = ('action', 'model_type')
    search_fields = ('user__email', 'ip_address')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'type', 'notifiable_type', 'read_at')
    list_filter = ('type', 'notifiable_type')

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserActivity, DailyMetric

@admin.register(UserActivity)
class UserActivityAdmin(ModelAdmin):
    list_display = ("user", "activity_type", "timestamp")
    list_filter = ("activity_type", "timestamp")
    search_fields = ("user__email", "activity_type")
    list_select_related = ("user",)

@admin.register(DailyMetric)
class DailyMetricAdmin(ModelAdmin):
    list_display = ("date", "total_lookups", "total_games", "new_users")
    list_filter = ("date",)
    ordering = ("-date",)

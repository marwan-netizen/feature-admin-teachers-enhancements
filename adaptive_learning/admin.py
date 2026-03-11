from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AdaptivePlan

@admin.register(AdaptivePlan)
class AdaptivePlanAdmin(ModelAdmin):
    list_display = ("user", "plan_name", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("plan_name",)
    list_select_related = ("user",)

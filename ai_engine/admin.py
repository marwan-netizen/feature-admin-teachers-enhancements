from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ChatSession

@admin.register(ChatSession)
class ChatSessionAdmin(ModelAdmin):
    list_display = ("user", "role", "created_at")
    list_filter = ("role", "created_at")
    search_fields = ("content", "user__email", "user__full_name")
    list_select_related = ("user",)
    readonly_fields = ("created_at", "updated_at")

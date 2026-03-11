from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import MediaBookmark

@admin.register(MediaBookmark)
class MediaBookmarkAdmin(ModelAdmin):
    list_display = ("title", "user", "source", "created_at")
    list_filter = ("source", "created_at")
    search_fields = ("title", "url")
    list_select_related = ("user",)

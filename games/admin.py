from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FlashcardSession, GameScore

@admin.register(FlashcardSession)
class FlashcardSessionAdmin(ModelAdmin):
    list_display = ("user", "created_at", "completed_at")
    list_select_related = ("user",)

@admin.register(GameScore)
class GameScoreAdmin(ModelAdmin):
    list_display = ("user", "game_type", "score", "achieved_at")
    list_filter = ("game_type", "achieved_at")
    list_select_related = ("user",)

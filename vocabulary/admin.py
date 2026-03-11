from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from .models import Word, Definition, WordOfTheDay, Bookmark, Lesson, UserLevel

class DefinitionInline(TabularInline):
    model = Definition
    extra = 1

@admin.register(Word)
class WordAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ("word", "cefr_level", "frequency_score", "created_at")
    list_filter = ("cefr_level",)
    search_fields = ("word",)
    inlines = [DefinitionInline]

@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ("title", "level", "created_at")
    list_filter = ("level",)
    search_fields = ("title", "description")
    filter_horizontal = ("words",)

@admin.register(UserLevel)
class UserLevelAdmin(ModelAdmin):
    list_display = ("user", "current_level", "vocabulary_size", "last_updated")
    list_filter = ("current_level",)
    list_select_related = ("user",)

@admin.register(WordOfTheDay)
class WordOfTheDayAdmin(ModelAdmin):
    list_display = ("word", "date")
    list_select_related = ("word",)

@admin.register(Bookmark)
class BookmarkAdmin(ModelAdmin):
    list_display = ("user", "word", "created_at")
    list_select_related = ("user", "word")

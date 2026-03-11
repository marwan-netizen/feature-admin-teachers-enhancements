from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Word, Definition, WordOfTheDay, Bookmark, Lesson, UserLevel

class WordResource(resources.ModelResource):
    class Meta:
        model = Word
        fields = ('id', 'word', 'phonetic', 'cefr_level', 'frequency_score')

class DefinitionInline(TabularInline):
    model = Definition
    extra = 1

@admin.register(Word)
class WordAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_classes = [WordResource]
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ("word", "phonetic", "cefr_level", "frequency_score", "created_at")
    list_filter = ("cefr_level",)
    search_fields = ("word",)
    inlines = [DefinitionInline]

@admin.register(WordOfTheDay)
class WordOfTheDayAdmin(ModelAdmin):
    list_display = ("word", "date")
    ordering = ("-date",)

@admin.register(Bookmark)
class BookmarkAdmin(ModelAdmin):
    list_display = ("user", "word", "created_at")
    search_fields = ("user__full_name", "word__word")

@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ("title", "level", "created_at")
    list_filter = ("level",)
    search_fields = ("title", "description")

@admin.register(UserLevel)
class UserLevelAdmin(ModelAdmin):
    list_display = ("user", "current_level", "vocabulary_size", "last_updated")
    list_filter = ("current_level",)

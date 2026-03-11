from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Test, Question, Option, StudentAnswer, Result, Evaluation

class OptionInline(TabularInline):
    model = Option
    extra = 1

class QuestionInline(TabularInline):
    model = Question
    extra = 1

@admin.register(Test)
class TestAdmin(ModelAdmin):
    list_display = ("test_name", "level", "skill", "teacher", "created_at")
    list_filter = ("level", "skill")
    search_fields = ("test_name", "content")
    inlines = [QuestionInline]
    list_select_related = ("teacher__user",)

@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("question_text", "test", "question_type", "difficulty_level")
    list_filter = ("question_type", "difficulty_level")
    search_fields = ("question_text",)
    inlines = [OptionInline]
    list_select_related = ("test",)

@admin.register(Option)
class OptionAdmin(ModelAdmin):
    list_display = ("option_text", "question", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("option_text",)
    list_select_related = ("question",)

@admin.register(StudentAnswer)
class StudentAnswerAdmin(ModelAdmin):
    list_display = ("student", "question", "created_at")
    search_fields = ("student__user__full_name", "question__question_text")
    list_select_related = ("student__user", "question__test")

@admin.register(Result)
class ResultAdmin(ModelAdmin):
    list_display = ("user", "test", "final_score", "created_at")
    list_filter = ("test__level", "test__skill")
    search_fields = ("user__full_name", "test__test_name")
    list_select_related = ("user", "test")

@admin.register(Evaluation)
class EvaluationAdmin(ModelAdmin):
    list_display = ("answer", "ai_score", "created_at")
    search_fields = ("answer__student__user__full_name", "ai_feedback")
    list_select_related = ("answer__student__user", "answer__question")

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import VocabularyService
from .models import Word, Bookmark, Lesson

class SmartDictionaryView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        word_data = None
        extra_data = None
        if query:
            service = VocabularyService()
            word_data = service.get_or_fetch_word(query)
            extra_data = service.get_synonyms_and_antonyms(query)

        return render(request, 'vocabulary/dictionary.html', {
            'query': query,
            'word': word_data,
            'extra': extra_data
        })

class WordOfTheDayView(View):
    def get(self, request):
        service = VocabularyService()
        word = service.get_word_of_the_day()
        return render(request, 'vocabulary/wotd.html', {'word': word})

class BookmarkToggleView(LoginRequiredMixin, View):
    def post(self, request, word_id):
        service = VocabularyService()
        is_bookmarked = service.toggle_bookmark(request.user, word_id)
        return JsonResponse({'status': 'success', 'is_bookmarked': is_bookmarked})

class LessonListView(View):
    def get(self, request):
        service = VocabularyService()
        lessons = service.get_lessons(request.GET.get('level'))
        return render(request, 'vocabulary/lessons.html', {'lessons': lessons})

class LessonDetailView(View):
    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        return render(request, 'vocabulary/lesson_detail.html', {'lesson': lesson})

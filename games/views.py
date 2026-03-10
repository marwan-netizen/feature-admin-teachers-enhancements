from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import GamesService

class FlashcardView(LoginRequiredMixin, View):
    def get(self, request):
        service = GamesService()
        cards = service.get_flashcards(request.user)
        return render(request, 'games/flashcards.html', {'cards': cards})

class SentenceCompletionView(View):
    def get(self, request):
        service = GamesService()
        exercises = service.get_sentence_completion_data()
        return render(request, 'games/sentence_completion.html', {'exercises': exercises})

class PronunciationPracticeView(View):
    def get(self, request):
        # We will use Web Speech API in the template
        word = request.GET.get('word', 'excellent')
        return render(request, 'games/pronunciation.html', {'word': word})

class WordNetworkView(View):
    def get(self, request):
        word = request.GET.get('word', 'education')
        return render(request, 'games/network.html', {'word': word})

class WordNetworkDataView(View):
    def get(self, request):
        from django.http import JsonResponse
        word = request.GET.get('word', 'education')
        service = GamesService()
        data = service.get_word_network(word)
        return JsonResponse(data)

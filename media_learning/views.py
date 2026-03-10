from django.shortcuts import render
from django.views import View
from .services import MediaLearningService

class ReadingSystemView(View):
    def get(self, request):
        topic = request.GET.get('topic', 'English_language')
        service = MediaLearningService()
        article = service.get_reading_material(topic)
        return render(request, 'media_learning/reading.html', {'article': article, 'topic': topic})

class PodcastExercisesView(View):
    def get(self, request):
        q = request.GET.get('q', 'English learning')
        service = MediaLearningService()
        podcasts = service.get_podcasts(q)
        return render(request, 'media_learning/podcasts.html', {'podcasts': podcasts, 'q': q})

class BookLibraryView(View):
    def get(self, request):
        q = request.GET.get('q', 'English grammar')
        service = MediaLearningService()
        books = service.get_books(q)
        return render(request, 'media_learning/books.html', {'books': books, 'q': q})

class YouGlishView(View):
    def get(self, request):
        word = request.GET.get('word', 'phenomenon')
        return render(request, 'media_learning/youglish.html', {'word': word})

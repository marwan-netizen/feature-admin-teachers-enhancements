from django.urls import path
from .views import ReadingSystemView, PodcastExercisesView, BookLibraryView, YouGlishView

app_name = 'media_learning'

urlpatterns = [
    path('reading/', ReadingSystemView.as_view(), name='reading'),
    path('podcasts/', PodcastExercisesView.as_view(), name='podcasts'),
    path('books/', BookLibraryView.as_view(), name='books'),
    path('youglish/', YouGlishView.as_view(), name='youglish'),
]

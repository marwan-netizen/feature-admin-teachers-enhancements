from django.urls import path
from .views import FlashcardView, SentenceCompletionView, PronunciationPracticeView, WordNetworkView, WordNetworkDataView

app_name = 'games'

urlpatterns = [
    path('flashcards/', FlashcardView.as_view(), name='flashcards'),
    path('sentence-completion/', SentenceCompletionView.as_view(), name='sentence_completion'),
    path('pronunciation/', PronunciationPracticeView.as_view(), name='pronunciation'),
    path('network/', WordNetworkView.as_view(), name='network'),
    path('network/data/', WordNetworkDataView.as_view(), name='network_data'),
]

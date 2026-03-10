from django.urls import path
from .views import GrammarTrainerView, CEFRDetectionView

app_name = 'grammar_analysis'

urlpatterns = [
    path('trainer/', GrammarTrainerView.as_view(), name='trainer'),
    path('cefr/', CEFRDetectionView.as_view(), name='cefr'),
]

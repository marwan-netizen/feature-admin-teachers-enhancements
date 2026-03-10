from django.contrib import admin
from django.urls import path, include
from vocabulary.views import WordOfTheDayView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('classroom/', include('classroom.urls')),
    path('testing/', include('testing.urls')),
    path('ai/', include('ai_engine.urls')),
    path('vocabulary/', include('vocabulary.urls', namespace='vocabulary')),
    path('games/', include('games.urls', namespace='games')),
    path('analysis/', include('grammar_analysis.urls', namespace='grammar_analysis')),
    path('media/', include('media_learning.urls', namespace='media_learning')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('', WordOfTheDayView.as_view(), name='home'),
]

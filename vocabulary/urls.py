from django.urls import path
from .views import SmartDictionaryView, WordOfTheDayView, BookmarkToggleView, LessonListView, LessonDetailView

app_name = 'vocabulary'

urlpatterns = [
    path('dictionary/', SmartDictionaryView.as_view(), name='dictionary'),
    path('wotd/', WordOfTheDayView.as_view(), name='wotd'),
    path('bookmark/<int:word_id>/', BookmarkToggleView.as_view(), name='bookmark_toggle'),
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
]

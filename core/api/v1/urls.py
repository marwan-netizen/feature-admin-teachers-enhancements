from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, ProfileViewSet, VocabularyViewSet, LessonViewSet, BookmarkViewSet
from testing.api_views import TestViewSet, ResultViewSet
from classroom.api_views import ClassroomViewSet, SessionViewSet, AssignmentViewSet, GradeViewSet
from analytics.api_views import ActivityViewSet, AdminMetricViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'tests', TestViewSet, basename='tests')
router.register(r'results', ResultViewSet, basename='results')
router.register(r'classrooms', ClassroomViewSet, basename='classrooms')
router.register(r'sessions', SessionViewSet, basename='sessions')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'grades', GradeViewSet, basename='grades')
router.register(r'vocabulary', VocabularyViewSet, basename='vocabulary')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'bookmarks', BookmarkViewSet, basename='bookmarks')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'admin/metrics', AdminMetricViewSet, basename='admin-metrics')

urlpatterns = [
    path('', include(router.urls)),
]

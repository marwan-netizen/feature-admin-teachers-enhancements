from django.contrib import admin
from django.urls import path, include
from vocabulary.views import WordOfTheDayView
from enterprise.services.audit import audit_log_view
from enterprise.services.diagnostics import diagnostic_center_view
from enterprise.ai.views import ai_insights_view

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', include('django_prometheus.urls')),
    path('', include('core.urls')),
    path('admin/enterprise/audit-logs/', audit_log_view, name='admin_audit_logs'),
    path('admin/enterprise/health/', diagnostic_center_view, name='admin_system_health'),
    path('admin/enterprise/ai-insights/', ai_insights_view, name='admin_ai_insights'),
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
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', WordOfTheDayView.as_view(), name='home'),
]

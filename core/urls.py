from django.urls import path, include
from . import views
from ai_engine import views as ai_views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('health/', views.health_check, name='health_check'),
    path('test-loading/', views.render_loading_test, name='test_loading'),
    path('strengthening/', ai_views.strengthening_plan, name='strengthening'),
    path('api/v1/', include('core.api.v1.urls')),
]

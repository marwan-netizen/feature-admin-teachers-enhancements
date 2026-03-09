from django.urls import path
from . import views

app_name = 'core'

from ai_engine import views as ai_views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('health/', views.health_check, name='health_check'),
    path('strengthening/', ai_views.strengthening_plan, name='strengthening'),
]

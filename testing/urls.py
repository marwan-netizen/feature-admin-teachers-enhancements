from django.urls import path
from . import views

app_name = 'testing'

urlpatterns = [
    path('test/start/', views.start_ai, name='start_ai'),
    path('test/check-status/', views.check_session_status, name='check_status'),
    path('test-instructions/', views.test_instructions, name='test_instructions'),

    # Reading
    path('test/reading/', views.reading_start, name='reading_start'),
    path('test/reading/q1/', views.reading_q1, name='reading_q1'),
    path('test/reading/submit/<str:q>/', views.submit_reading, name='submit_reading'),
    path('test/reading/done/', views.reading_done, name='reading_done'),

    # Writing
    path('test/writing/', views.writing_start, name='writing_start'),
    path('test/writing/submit/', views.submit_writing, name='submit_writing'),
    path('test/writing/done/', views.writing_done, name='writing_done'),

    # Listening
    path('test/listening/', views.listening_start, name='listening_start'),
    path('test/listening/submit/<str:q>/', views.submit_listening, name='submit_listening'),
    path('test/listening/done/', views.listening_done, name='listening_done'),

    # Speaking
    path('test/speaking/', views.speaking_start, name='speaking_start'),
    path('test/speaking/submit/', views.submit_speaking, name='submit_speaking'),
    path('test/speaking/done/', views.speaking_done, name='speaking_done'),

    # Results
    path('test/results/', views.results, name='results'),
]

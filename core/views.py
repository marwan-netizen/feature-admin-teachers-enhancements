"""
Global views for the core application.

Includes landing pages and system health monitoring.
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def index(request):
    """
    Renders the main landing page of the platform.
    """
    return render(request, 'core/index.html')

def how_it_works(request):
    """
    Renders the informational "How it Works" page.
    """
    return render(request, 'core/how_it_works.html')

from django.core.cache import cache

def health_check(request):
    """
    System health check endpoint for monitoring and load balancers.
    Performs checks for Database, Redis, and Celery.
    """
    health = {'status': 'healthy', 'checks': {}}

    # DB Check
    try:
        connection.ensure_connection()
        health['checks']['database'] = 'ok'
    except Exception as e:
        health['status'] = 'unhealthy'
        health['checks']['database'] = str(e)

    # Cache/Redis Check
    try:
        cache.set('health_check', 'ok', 5)
        if cache.get('health_check') == 'ok':
            health['checks']['redis'] = 'ok'
        else:
            raise Exception("Cache get failed")
    except Exception as e:
        health['status'] = 'unhealthy'
        health['checks']['redis'] = str(e)

    # Celery Check
    try:
        from lingopulse.celery import app as celery_app
        inspector = celery_app.control.inspect()
        stats = inspector.stats()
        if stats:
            health['checks']['celery'] = 'ok'
        else:
            health['checks']['celery'] = 'no workers detected'
            # Don't mark as unhealthy just because workers are busy/temporarily unavailable
            # but in production we might want at least one worker.
    except Exception as e:
        health['checks']['celery'] = str(e)

    return JsonResponse(health, status=200 if health['status'] == 'healthy' else 503)

def render_loading_test(request):
    """
    Renders the loading page for visual verification.
    """
    from django.shortcuts import render
    return render(request, 'testing/loading.html', {'task_id': 'test-id'})

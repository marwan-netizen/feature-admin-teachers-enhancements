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

def health_check(request):
    """
    System health check endpoint for monitoring and load balancers.

    Performs basic dependency checks (e.g., Database connectivity).
    """
    health = {'status': 'healthy', 'checks': {}}

    # DB Check
    try:
        connection.ensure_connection()
        health['checks']['database'] = 'ok'
    except Exception as e:
        health['status'] = 'unhealthy'
        health['checks']['database'] = str(e)

    return JsonResponse(health, status=200 if health['status'] == 'healthy' else 503)

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def index(request):
    return render(request, 'core/index.html')

def how_it_works(request):
    return render(request, 'core/how_it_works.html')

def health_check(request):
    health = {'status': 'healthy', 'checks': {}}

    # DB Check
    try:
        connection.ensure_connection()
        health['checks']['database'] = 'ok'
    except Exception as e:
        health['status'] = 'unhealthy'
        health['checks']['database'] = str(e)

    return JsonResponse(health, status=200 if health['status'] == 'healthy' else 503)

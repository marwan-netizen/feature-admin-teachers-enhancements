"""
Global middleware for the LingoPulse AI platform.
"""

import logging
import traceback
from django.http import JsonResponse
from django.conf import settings

logger = logging.getLogger(__name__)

class ExceptionHandlerMiddleware:
    """
    Middleware for centralized exception handling and structured logging.
    """
    def __init__(self, get_response):
        """
        Initializes the middleware.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes the request/response cycle.
        """
        return self.get_response(request)

    def process_exception(self, request, exception):
        """
        Handles unhandled exceptions by logging them and returning a JSON response.

        In DEBUG mode, returns None to allow Django's built-in debugger to run.
        """
        # Structured log
        log_data = {
            'message': str(exception),
            'method': request.method,
            'path': request.get_full_path(),
            'user_id': request.user.user_id if request.user.is_authenticated else None,
            'traceback': traceback.format_exc()
        }
        logger.error(f"Unhandled Exception: {log_data}")

        if settings.DEBUG:
            return None # Let Django's default debugger handle it

        return JsonResponse({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred. Our engineers have been notified.'
        }, status=500)

class RBACMiddleware:
    """
    Middleware for basic Role-Based Access Control.
    Enforces that only admins can access /admin/.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.path.startswith('/admin/login'):
            if not request.user.is_authenticated or request.user.role != 'admin':
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden("Access Denied: Administrative privileges required.")

        response = self.get_response(request)
        return response

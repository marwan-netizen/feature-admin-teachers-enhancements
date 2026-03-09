import logging
import traceback
from django.http import JsonResponse
from django.conf import settings

logger = logging.getLogger(__name__)

class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        # Structured log
        log_data = {
            'message': str(exception),
            'method': request.method,
            'path': request.get_full_path(),
            'user_id': request.user.id if request.user.is_authenticated else None,
            'traceback': traceback.format_exc()
        }
        logger.error(f"Unhandled Exception: {log_data}")

        if settings.DEBUG:
            return None # Let Django's default debugger handle it

        return JsonResponse({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred. Our engineers have been notified.'
        }, status=500)

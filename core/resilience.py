"""
Centralized resilience mechanisms for the LingoPulse AI platform.
"""

import logging
from functools import wraps
from pycircuitbreaker import circuit

logger = logging.getLogger(__name__)

# Define common circuit breakers
ai_generation_cb = circuit(
    failure_threshold=5,
    recovery_timeout=60,
    name='ai_generation'
)

external_api_cb = circuit(
    failure_threshold=10,
    recovery_timeout=30,
    name='external_api'
)

def with_resilience(cb=None, fallback_func=None):
    """
    Decorator to wrap a function with circuit breaker and fallback.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if cb:
                try:
                    # pycircuitbreaker can be used as a context manager or decorator
                    with cb:
                        return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Resilience triggered for {func.__name__}: {str(e)}")
                    if fallback_func:
                        return fallback_func(*args, **kwargs)
                    raise
            return func(*args, **kwargs)
        return wrapper
    return decorator

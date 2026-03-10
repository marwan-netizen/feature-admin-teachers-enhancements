"""
Custom exception classes for the LingoPulse AI platform.
"""

class LingoPulseException(Exception):
    """
    Base exception for all LingoPulse AI specific errors.
    """
    pass

class AIServiceError(LingoPulseException):
    """
    Raised when an interaction with an AI provider fails.
    """
    pass

class GenerationError(AIServiceError):
    """
    Raised when AI content generation (tests, passages) fails.
    """
    pass

class EvaluationError(AIServiceError):
    """
    Raised when AI evaluation (grading, feedback) fails.
    """
    pass

class EntityNotFoundError(LingoPulseException):
    """
    Raised when a requested domain entity cannot be found.
    """
    pass

class LingoPulseException(Exception):
    """Base exception for LingoPulse AI."""
    pass

class AIServiceError(LingoPulseException):
    """Raised when an AI service fails."""
    pass

class GenerationError(AIServiceError):
    """Raised when content generation fails."""
    pass

class EvaluationError(AIServiceError):
    """Raised when evaluation fails."""
    pass

class EntityNotFoundError(LingoPulseException):
    """Raised when a requested entity is not found."""
    pass

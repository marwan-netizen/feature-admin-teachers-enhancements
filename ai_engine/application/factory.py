"""
Factory for instantiating AI services with concrete providers.
"""

from ai_engine.infrastructure.adapters.groq_adapter import GroqProvider
from ai_engine.infrastructure.adapters.gemini_adapter import GeminiProvider
from ai_engine.infrastructure.adapters.openrouter_adapter import OpenRouterProvider
from .services import AIService

class AIServiceFactory:
    """
    Factory class to create instances of AIService.
    """
    @staticmethod
    def create_standard_service() -> AIService:
        """
        Creates a standard AIService with default providers.

        Returns:
            AIService: An instance of AIService configured with Groq, Gemini, and OpenRouter.
        """
        return AIService(
            text_generator=GroqProvider(),
            evaluator=GeminiProvider(),
            listening_generator=OpenRouterProvider()
        )

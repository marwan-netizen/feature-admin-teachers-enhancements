from ai_engine.infrastructure.adapters.groq_adapter import GroqProvider
from ai_engine.infrastructure.adapters.gemini_adapter import GeminiProvider
from ai_engine.infrastructure.adapters.openrouter_adapter import OpenRouterProvider
from .services import AIService

class AIServiceFactory:
    @staticmethod
    def create_standard_service() -> AIService:
        return AIService(
            text_generator=GroqProvider(),
            evaluator=GeminiProvider(),
            listening_generator=OpenRouterProvider()
        )

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class TextGenerationProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: str = "", json_mode: bool = False) -> str:
        pass

class EvaluationProvider(ABC):
    @abstractmethod
    def evaluate(self, text: str, skill: str) -> Dict[str, Any]:
        pass

class TTSProvider(ABC):
    @abstractmethod
    def text_to_speech(self, text: str) -> str:
        """Returns URL or path to the audio file."""
        pass

class StreamingProvider(ABC):
    @abstractmethod
    def stream_explanation(self, question: str, student_answer: str, correct_answer: str):
        pass

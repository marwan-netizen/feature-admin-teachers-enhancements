"""
Interface definitions (Ports) for AI providers.

These abstract base classes define the contracts that any concrete AI provider
adapter must implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class TextGenerationProvider(ABC):
    """
    Interface for text generation capabilities.
    """
    @abstractmethod
    def generate(self, prompt: str, system_prompt: str = "", json_mode: bool = False) -> str:
        """
        Generates text based on a prompt.

        Args:
            prompt: The user prompt.
            system_prompt: Optional system-level instructions.
            json_mode: Whether to force the output into a JSON object format.

        Returns:
            str: The generated text.
        """
        pass

class EvaluationProvider(ABC):
    """
    Interface for student response evaluation capabilities.
    """
    @abstractmethod
    def evaluate(self, text: str, skill: str) -> Dict[str, Any]:
        """
        Evaluates a student's response.

        Args:
            text: The text to evaluate.
            skill: The skill category (e.g., 'writing').

        Returns:
            Dict[str, Any]: Evaluation result containing score and feedback.
        """
        pass

class TTSProvider(ABC):
    """
    Interface for Text-to-Speech capabilities.
    """
    @abstractmethod
    def text_to_speech(self, text: str) -> str:
        """
        Converts text to an audio resource.

        Args:
            text: The text to convert.

        Returns:
            str: URL or file path to the generated audio.
        """
        pass

class StreamingProvider(ABC):
    """
    Interface for real-time streaming capabilities.
    """
    @abstractmethod
    def stream_explanation(self, question: str, student_answer: str, correct_answer: str):
        """
        Streams an explanation for a test question.

        Args:
            question: The original test question.
            student_answer: The answer provided by the student.
            correct_answer: The expected correct answer.
        """
        pass

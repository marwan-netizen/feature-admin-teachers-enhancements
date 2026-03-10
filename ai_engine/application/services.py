"""
Application services for the AI Engine module.

This module contains the primary business logic for interacting with AI providers
to generate educational content and evaluate student performance.
"""

import json
import logging
from typing import Dict, Any, List, Optional
from ai_engine.domain.entities import TestDTO, QuestionDTO, OptionDTO, ComprehensiveTestDTO
from ai_engine.domain.interfaces import TextGenerationProvider, EvaluationProvider, TTSProvider
from core.exceptions import GenerationError, EvaluationError

logger = logging.getLogger(__name__)

class AIService:
    """
    Service responsible for coordinating AI-powered features.

    This service acts as the primary interface for other modules to interact
    with various AI providers for test generation and evaluation.
    """
    def __init__(
        self,
        text_generator: TextGenerationProvider,
        evaluator: EvaluationProvider,
        listening_generator: Optional[TextGenerationProvider] = None
    ):
        """
        Initializes the AIService with necessary providers.

        Args:
            text_generator: Provider for general text generation (e.g., Reading/Writing tests).
            evaluator: Provider for evaluating student responses (e.g., Writing/Speaking).
            listening_generator: Optional provider for listening tests. Defaults to text_generator.
        """
        self.text_generator = text_generator
        self.evaluator = evaluator
        # In this specific app, OpenRouter handles both text and TTS for listening
        self.listening_generator = listening_generator or text_generator

    def generate_comprehensive_test(self) -> ComprehensiveTestDTO:
        """
        Generates a full set of tests covering Reading, Writing, and Speaking.

        Returns:
            ComprehensiveTestDTO: A DTO containing the generated tests for all three skills.

        Raises:
            GenerationError: If the AI provider fails to generate valid test content.
        """
        prompt = """You are an expert English language test creator for beginners. Generate a brand new, unique, and engaging reading, writing, and speaking test.
Return ONLY a valid JSON object matching the exact structure below.

{
  "reading": {
    "passage": "A completely new original story of about 100-150 words.",
    "questions": [
      {
        "text": "A multiple choice question about the passage",
        "options": ["Correct Answer", "Wrong Option 1", "Wrong Option 2", "Wrong Option 3"],
        "correct_index": 0
      }
    ]
  },
  "writing": {
    "topic": "A completely new, interesting writing topic for beginners."
  },
  "speaking": {
    "passage": "A completely new short passage (20-30 words) for the student to read aloud."
  }
}"""
        try:
            content = self.text_generator.generate(prompt, system_prompt="You only reply with valid, raw JSON.", json_mode=True)
            data = json.loads(content)

            reading_dto = TestDTO(
                name='Dynamic Reading',
                level='Beginner',
                skill='reading_dynamic',
                content=data['reading']['passage'],
                questions=[
                    QuestionDTO(
                        text=q['text'],
                        options=[
                            OptionDTO(text=opt_text, is_correct=(idx == q['correct_index']))
                            for idx, opt_text in enumerate(q['options'])
                        ]
                    ) for q in data['reading']['questions']
                ]
            )

            writing_dto = TestDTO(
                name='Dynamic Writing',
                level='Beginner',
                skill='writing_dynamic',
                content=data['writing']['topic']
            )

            speaking_dto = TestDTO(
                name='Dynamic Speaking',
                level='Beginner',
                skill='speaking_dynamic',
                content=data['speaking']['passage']
            )

            return ComprehensiveTestDTO(reading=reading_dto, writing=writing_dto, speaking=speaking_dto)

        except Exception as e:
            logger.error(f"Failed to generate tests: {str(e)}")
            raise GenerationError(f"Comprehensive test generation failed: {str(e)}")

    def generate_listening_test(self) -> List[TestDTO]:
        """
        Generates a set of listening tests with associated audio or scripts.

        Returns:
            List[TestDTO]: A list of TestDTOs representing the generated listening tests.

        Raises:
            GenerationError: If the listening test generation or TTS conversion fails.
        """
        prompt = "Generate 3 listening tests for English beginners. Each should have a short script (50-80 words) and 5 MCQs. Return ONLY raw JSON array."
        try:
            content = self.listening_generator.generate(prompt)
            data = json.loads(content.strip('`json\n '))

            tests = []
            for test_data in data:
                audio_path = ""
                if isinstance(self.listening_generator, TTSProvider):
                    audio_path = self.listening_generator.text_to_speech(test_data['script'])

                test_dto = TestDTO(
                    name='Dynamic Listening',
                    level='Beginner',
                    skill='listening_dynamic',
                    content=audio_path or test_data['script'],
                    questions=[
                        QuestionDTO(
                            text=q['text'],
                            options=[
                                OptionDTO(text=opt_text, is_correct=(idx == q['correct_index']))
                                for idx, opt_text in enumerate(q['options'])
                            ]
                        ) for q in test_data['questions']
                    ]
                )
                tests.append(test_dto)
            return tests
        except Exception as e:
            logger.error(f"Failed to generate listening tests: {str(e)}")
            raise GenerationError(f"Listening test generation failed: {str(e)}")

    def evaluate_response(self, text: str, skill: str) -> Dict[str, Any]:
        """
        Evaluates a student's response for a specific skill.

        Args:
            text: The student's input (essay text or speaking transcription).
            skill: The skill being evaluated ('writing' or 'speaking').

        Returns:
            Dict[str, Any]: A dictionary containing the score and qualitative feedback.

        Raises:
            EvaluationError: If the evaluation provider fails.
        """
        try:
            return self.evaluator.evaluate(text, skill)
        except Exception as e:
            logger.error(f"AI evaluation failed: {str(e)}")
            raise EvaluationError(f"Evaluation failed: {str(e)}")

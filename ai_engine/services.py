import json
import logging
from typing import Dict, Any, List, Optional
from django.db import transaction
from testing.models import Test, Question, Option
from .adapters.groq_adapter import GroqProvider
from .adapters.gemini_adapter import GeminiProvider
from .adapters.openrouter_adapter import OpenRouterProvider

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.groq = GroqProvider()
        self.gemini = GeminiProvider()
        self.openrouter = OpenRouterProvider()

    def generate_comprehensive_test(self) -> Dict[str, Any]:
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
            content = self.groq.generate(prompt, system_prompt="You only reply with valid, raw JSON.", json_mode=True)
            data = json.loads(content)

            with transaction.atomic():
                test_ids = {}
                # Reading
                reading_test = Test.objects.create(
                    test_name='Dynamic Reading', level='Beginner', skill='reading_dynamic', content=data['reading']['passage']
                )
                test_ids['reading'] = reading_test.test_id
                for q in data['reading']['questions']:
                    new_q = Question.objects.create(test=reading_test, question_text=q['text'], question_type='mcq')
                    for idx, opt_text in enumerate(q['options']):
                        Option.objects.create(question=new_q, option_text=opt_text, is_correct=(idx == q['correct_index']))

                # Writing
                writing_test = Test.objects.create(
                    test_name='Dynamic Writing', level='Beginner', skill='writing_dynamic', content=data['writing']['topic']
                )
                test_ids['writing'] = writing_test.test_id

                # Speaking
                speaking_test = Test.objects.create(
                    test_name='Dynamic Speaking', level='Beginner', skill='speaking_dynamic', content=data['speaking']['passage']
                )
                test_ids['speaking'] = speaking_test.test_id

                return test_ids
        except Exception as e:
            logger.error(f"Failed to generate tests: {str(e)}")
            return {}

    def generate_listening_test(self) -> Optional[int]:
        prompt = "Generate 3 listening tests for English beginners. Each should have a short script (50-80 words) and 5 MCQs. Return ONLY raw JSON array."
        try:
            content = self.openrouter.generate(prompt)
            data = json.loads(content.strip('`json\n '))

            with transaction.atomic():
                first_test_id = None
                for test_data in data:
                    audio_path = self.openrouter.text_to_speech(test_data['script'])

                    test = Test.objects.create(
                        test_name='Dynamic Listening',
                        level='Beginner',
                        skill='listening_dynamic',
                        content=audio_path or test_data['script']
                    )
                    if not first_test_id: first_test_id = test.test_id

                    for q in test_data['questions']:
                        new_q = Question.objects.create(test=test, question_text=q['text'], question_type='mcq')
                        for idx, opt_text in enumerate(q['options']):
                            Option.objects.create(question=new_q, option_text=opt_text, is_correct=(idx == q['correct_index']))
                return first_test_id
        except Exception as e:
            logger.error(f"Failed to generate listening tests: {str(e)}")
            return None

    def evaluate_response(self, text: str, skill: str) -> Dict[str, Any]:
        return self.gemini.evaluate(text, skill)

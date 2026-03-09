import os
import json
import logging
import google.generativeai as genai
from ai_engine.domain.interfaces import EvaluationProvider

logger = logging.getLogger(__name__)

class GeminiProvider(EvaluationProvider):
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def evaluate(self, text: str, skill: str) -> dict:
        if not self.api_key:
            return {'score': 75, 'feedback': 'Mock feedback (API Key missing)'}

        if skill == 'writing':
            prompt = f"""Evaluate this writing response. Reply ONLY with JSON: {{"score":N, "feedback":"..."}} \n\n Response: {text}"""
        else:
            prompt = f"""Evaluate this speaking transcription. Reply ONLY with JSON: {{"score":N, "feedback":"..."}} \n\n Transcription: {text}"""

        try:
            response = self.model.generate_content(prompt)
            content = response.text.strip('`json\n ')
            return json.loads(content)
        except Exception as e:
            logger.error(f"Gemini evaluation failed: {str(e)}")
            return {'score': 50, 'feedback': 'AI evaluation error.'}

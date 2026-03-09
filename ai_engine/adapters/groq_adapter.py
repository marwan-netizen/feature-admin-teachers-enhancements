import os
import requests
import json
import logging
from ai_engine.interfaces import TextGenerationProvider

logger = logging.getLogger(__name__)

class GroqProvider(TextGenerationProvider):
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        self.url = 'https://api.groq.com/openai/v1/chat/completions'

    def generate(self, prompt: str, system_prompt: str = "", json_mode: bool = False) -> str:
        if not self.api_key:
            logger.error("Groq API key is missing.")
            raise ValueError("Groq API key is missing.")

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'llama-3.1-8b-instant',
            'messages': [
                {'role': 'system', 'content': system_prompt or 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.8,
        }
        if json_mode:
            payload['response_format'] = {'type': 'json_object'}

        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            logger.error(f"Groq generation failed: {str(e)}")
            raise

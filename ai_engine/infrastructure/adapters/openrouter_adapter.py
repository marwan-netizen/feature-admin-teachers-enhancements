"""
OpenRouter adapter for text generation and TTS.
"""

import os
import json
import logging
import requests
import uuid
import urllib.parse
from django.conf import settings
from ai_engine.domain.interfaces import TextGenerationProvider, TTSProvider

logger = logging.getLogger(__name__)

class OpenRouterProvider(TextGenerationProvider, TTSProvider):
    """
    Concrete implementation of TextGenerationProvider and TTSProvider via OpenRouter.
    """
    def __init__(self):
        """
        Initializes the OpenRouter provider with API credentials.
        """
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.url = 'https://openrouter.ai/api/v1/chat/completions'

    def generate(self, prompt: str, system_prompt: str = "", json_mode: bool = False) -> str:
        """
        Generates text using OpenRouter's meta-llama model.

        Args:
            prompt: The user prompt.
            system_prompt: Optional system instructions.
            json_mode: Whether to request JSON output.

        Returns:
            str: The generated content.

        Raises:
            ValueError: If the OpenRouter API key is missing.
            Exception: If the API request fails.
        """
        if not self.api_key:
            logger.error("OpenRouter API key is missing.")
            raise ValueError("OpenRouter API key is missing.")

        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        payload = {
            'model': 'meta-llama/llama-3.3-70b-instruct:free',
            'messages': [{'role': 'user', 'content': prompt}]
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            logger.error(f"OpenRouter generation failed: {str(e)}")
            raise

    def text_to_speech(self, text: str) -> str:
        """
        Converts text to speech using Google Translate TTS (legacy behavior).

        Args:
            text: The text to convert to audio.

        Returns:
            str: Relative URL to the generated MP3 file, or empty string if failed.
        """
        # Implementation using Google Translate TTS as in original code
        encoded_text = urllib.parse.quote(text[:500])
        audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=gtx&q={encoded_text}&tl=en-US"

        try:
            audio_res = requests.get(audio_url, timeout=30)
            if audio_res.status_code == 200:
                file_name = f'dynamic_listening_{uuid.uuid4()}.mp3'
                dir_path = os.path.join(settings.MEDIA_ROOT, 'audio')
                os.makedirs(dir_path, exist_ok=True)
                full_path = os.path.join(dir_path, file_name)
                with open(full_path, 'wb') as f:
                    f.write(audio_res.content)
                return f"{settings.MEDIA_URL}audio/{file_name}"
        except Exception as e:
            logger.error(f"TTS generation failed: {str(e)}")

        return ""

import httpx
import logging
from django.conf import settings
from typing import List, Optional
from core.dtos.base import WordDefinitionDTO, SynonymAntonymDTO, ExampleSentenceDTO
from .dictionary import BaseExternalService

logger = logging.getLogger(__name__)

class WordsAPIService(BaseExternalService):
    BASE_URL = "https://wordsapiv1.p.rapidapi.com/words/"

    def __init__(self):
        super().__init__()
        self.headers = {
            "X-RapidAPI-Key": settings.WORDS_API_KEY,
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }

    def get_details(self, word: str) -> Optional[dict]:
        if not settings.WORDS_API_KEY: return None
        try:
            response = self.client.get(f"{self.BASE_URL}{word}", headers=self.headers)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            logger.error(f"Error fetching from WordsAPI for {word}: {e}")
        return None

class OpenSubtitlesService(BaseExternalService):
    BASE_URL = "https://api.opensubtitles.com/api/v1/"

    def __init__(self):
        super().__init__()
        self.headers = {
            "Api-Key": settings.OPEN_SUBTITLES_API_KEY,
            "User-Agent": "LingoPulseAI v1.0"
        }

    def search_subtitles(self, query: str):
        if not settings.OPEN_SUBTITLES_API_KEY: return []
        try:
            response = self.client.get(f"{self.BASE_URL}subtitles?query={query}", headers=self.headers)
            if response.status_code == 200:
                return response.json().get('data', [])
        except Exception as e:
            logger.error(f"Error fetching from OpenSubtitles: {e}")
        return []

class QuotableService(BaseExternalService):
    BASE_URL = "https://api.quotable.io/random"

    def get_random_quote(self):
        try:
            response = self.client.get(self.BASE_URL)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            logger.error(f"Error fetching quote: {e}")
        return None

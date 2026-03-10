import httpx
import logging
from django.conf import settings
from django.core.cache import cache
from typing import List, Optional
from core.dtos.base import WordDefinitionDTO, SynonymAntonymDTO

logger = logging.getLogger(__name__)

class BaseExternalService:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.client = httpx.Client(timeout=timeout)

    def _get_cache_key(self, prefix: str, identifier: str) -> str:
        return f"{prefix}:{identifier.lower()}"

class FreeDictionaryService(BaseExternalService):
    BASE_URL = settings.FREE_DICTIONARY_API_URL

    def get_definition(self, word: str) -> List[WordDefinitionDTO]:
        cache_key = self._get_cache_key("free_dict", word)
        cached_data = cache.get(cache_key)
        if cached_data:
            return [WordDefinitionDTO.model_validate(d) for d in cached_data]

        from core.resilience import external_api_cb
        try:
            with external_api_cb:
                response = self.client.get(f"{self.BASE_URL}{word}")
                if response.status_code == 200:
                    data = response.json()
                    cache.set(cache_key, data, timeout=86400)  # Cache for 24h
                    return [WordDefinitionDTO.model_validate(d) for d in data]
        except Exception as e:
            logger.error(f"Error fetching definition for {word} from FreeDictionary: {e}")
        return []

class DatamuseService(BaseExternalService):
    BASE_URL = "https://api.datamuse.com/words"

    def get_synonyms(self, word: str) -> List[SynonymAntonymDTO]:
        cache_key = self._get_cache_key("datamuse_syn", word)
        cached_data = cache.get(cache_key)
        if cached_data:
            return [SynonymAntonymDTO.model_validate(d) for d in cached_data]

        try:
            response = self.client.get(f"{self.BASE_URL}?rel_syn={word}")
            if response.status_code == 200:
                data = response.json()
                cache.set(cache_key, data, timeout=86400)
                return [SynonymAntonymDTO.model_validate(item) for item in data]
        except Exception as e:
            logger.error(f"Error fetching synonyms for {word} from Datamuse: {e}")
        return []

    def get_antonyms(self, word: str) -> List[SynonymAntonymDTO]:
        cache_key = self._get_cache_key("datamuse_ant", word)
        cached_data = cache.get(cache_key)
        if cached_data:
            return [SynonymAntonymDTO.model_validate(d) for d in cached_data]

        try:
            response = self.client.get(f"{self.BASE_URL}?rel_ant={word}")
            if response.status_code == 200:
                data = response.json()
                cache.set(cache_key, data, timeout=86400)
                return [SynonymAntonymDTO.model_validate(item) for item in data]
        except Exception as e:
            logger.error(f"Error fetching antonyms for {word} from Datamuse: {e}")
        return []

class LinguaRobotService(BaseExternalService):
    BASE_URL = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/"

    def __init__(self):
        super().__init__()
        self.headers = {
            "X-RapidAPI-Key": settings.LINGUA_ROBOT_API_KEY,
            "X-RapidAPI-Host": "lingua-robot.p.rapidapi.com"
        }

    def get_entry(self, word: str) -> Optional[dict]:
        if not settings.LINGUA_ROBOT_API_KEY:
            return None

        cache_key = self._get_cache_key("lingua_robot", word)
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        try:
            response = self.client.get(f"{self.BASE_URL}{word}", headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                cache.set(cache_key, data, timeout=86400)
                return data
        except Exception as e:
            logger.error(f"Error fetching entry for {word} from LinguaRobot: {e}")
        return None

class EnglishRandomWordsService(BaseExternalService):
    BASE_URL = "https://random-word-api.herokuapp.com/word"

    def get_random_word(self) -> Optional[str]:
        try:
            response = self.client.get(self.BASE_URL)
            if response.status_code == 200:
                return response.json()[0]
        except Exception as e:
            logger.error(f"Error fetching random word: {e}")
        return None

class TatoebaService(BaseExternalService):
    # This is a simplified mock as Tatoeba doesn't have a very friendly public REST API for direct word lookup
    # Often developers use exports, but there are some third-party wrappers or specific endpoints.
    # We will implement a placeholder that could be expanded.
    def get_examples(self, word: str) -> List[str]:
        return [f"This is an example sentence using the word {word}."]

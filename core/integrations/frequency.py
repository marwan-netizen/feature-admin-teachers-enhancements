import httpx
import logging
from django.conf import settings
from .dictionary import BaseExternalService

logger = logging.getLogger(__name__)

class WordFrequencyService(BaseExternalService):
    BASE_URL = "https://api.datamuse.com/words"

    def get_frequency(self, word: str) -> float:
        try:
            # Datamuse returns frequency tags (e.g. f: 12.3456)
            response = self.client.get(f"{self.BASE_URL}?sp={word}&md=f&max=1")
            if response.status_code == 200:
                data = response.json()
                if data:
                    tags = data[0].get('tags', [])
                    for t in tags:
                        if t.startswith('f:'):
                            return float(t.split(':')[1])
        except Exception as e:
            logger.error(f"Error fetching frequency for {word}: {e}")
        return 0.0

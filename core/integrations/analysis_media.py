import httpx
import logging
import hashlib
import time
from django.conf import settings
from typing import List, Optional
from core.dtos.base import GrammarAnalysisDTO, GrammarIssueDTO, MediaContentDTO
from .dictionary import BaseExternalService

logger = logging.getLogger(__name__)

class LanguageToolService(BaseExternalService):
    BASE_URL = settings.LANGUAGE_TOOL_API_URL

    def check_text(self, text: str) -> GrammarAnalysisDTO:
        try:
            response = self.client.post(self.BASE_URL, data={'text': text, 'language': 'en-US'})
            if response.status_code == 200:
                data = response.json()
                issues = []
                for match in data.get('matches', []):
                    issues.append(GrammarIssueDTO(
                        message=match['message'],
                        short_message=match.get('shortMessage'),
                        offset=match['offset'],
                        length=match['length'],
                        replacements=[r['value'] for r in match.get('replacements', [])[:5]],
                        rule_id=match['rule']['id'],
                        category=match['rule']['category']['id']
                    ))
                return GrammarAnalysisDTO(text=text, issues=issues)
        except Exception as e:
            logger.error(f"Error checking text with LanguageTool: {e}")
        return GrammarAnalysisDTO(text=text, issues=[])

class WikipediaService(BaseExternalService):
    BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def get_summary(self, title: str) -> Optional[MediaContentDTO]:
        try:
            response = self.client.get(f"{self.BASE_URL}{title}")
            if response.status_code == 200:
                data = response.json()
                return MediaContentDTO(
                    title=data['title'],
                    content=data['extract'],
                    url=data['content_urls']['desktop']['page'],
                    thumbnail=data.get('thumbnail', {}).get('source'),
                    source="Wikipedia"
                )
        except Exception as e:
            logger.error(f"Error fetching Wikipedia summary for {title}: {e}")
        return None

class PodcastIndexService(BaseExternalService):
    BASE_URL = "https://api.podcastindex.org/api/1.0/"

    def search_podcasts(self, q: str) -> List[MediaContentDTO]:
        if not settings.PODCAST_INDEX_API_KEY:
            return []

        api_key = settings.PODCAST_INDEX_API_KEY
        api_secret = settings.PODCAST_INDEX_API_SECRET
        epoch_time = int(time.time())
        data_to_hash = api_key + api_secret + str(epoch_time)
        sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()

        headers = {
            'X-Auth-Key': api_key,
            'X-Auth-Date': str(epoch_time),
            'Authorization': sha_1,
            'User-Agent': 'LingoPulseAI/1.0'
        }

        try:
            response = self.client.get(f"{self.BASE_URL}search/byterm?q={q}", headers=headers)
            if response.status_code == 200:
                data = response.json()
                results = []
                for item in data.get('feeds', []):
                    results.append(MediaContentDTO(
                        title=item['title'],
                        content=item['description'],
                        url=item['url'],
                        thumbnail=item['image'],
                        source="PodcastIndex"
                    ))
                return results
        except Exception as e:
            logger.error(f"Error searching podcasts for {q}: {e}")
        return []

class GoogleBooksService(BaseExternalService):
    BASE_URL = "https://www.googleapis.com/books/v1/volumes"

    def search_books(self, q: str) -> List[MediaContentDTO]:
        params = {'q': q}
        if settings.GOOGLE_BOOKS_API_KEY:
            params['key'] = settings.GOOGLE_BOOKS_API_KEY

        try:
            response = self.client.get(self.BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                results = []
                for item in data.get('items', []):
                    info = item['volumeInfo']
                    results.append(MediaContentDTO(
                        title=info['title'],
                        content=info.get('description', ''),
                        url=info.get('infoLink'),
                        thumbnail=info.get('imageLinks', {}).get('thumbnail'),
                        source="GoogleBooks"
                    ))
                return results
        except Exception as e:
            logger.error(f"Error searching books for {q}: {e}")
        return []

class ConceptNetService(BaseExternalService):
    BASE_URL = "https://api.conceptnet.io/c/en/"

    def get_related_terms(self, word: str) -> List[dict]:
        try:
            response = self.client.get(f"{self.BASE_URL}{word.lower()}")
            if response.status_code == 200:
                return response.json().get('edges', [])
        except Exception as e:
            logger.error(f"Error fetching ConceptNet data for {word}: {e}")
        return []

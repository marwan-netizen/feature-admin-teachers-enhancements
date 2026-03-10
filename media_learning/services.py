import logging
from typing import List
from core.integrations.analysis_media import WikipediaService, PodcastIndexService, GoogleBooksService
from core.integrations.extra_apis import OpenSubtitlesService

logger = logging.getLogger(__name__)

class MediaLearningService:
    def __init__(self):
        self.wiki = WikipediaService()
        self.podcast = PodcastIndexService()
        self.books = GoogleBooksService()
        self.subtitles = OpenSubtitlesService()

    def get_reading_material(self, topic: str):
        return self.wiki.get_summary(topic)

    def get_podcasts(self, query: str):
        return self.podcast.search_podcasts(query)

    def get_books(self, query: str):
        return self.books.search_books(query)

    def get_drama_dialogues(self, query: str) -> List[dict]:
        """Fetch drama dialogue snippets using OpenSubtitles API."""
        return self.subtitles.search_subtitles(query)

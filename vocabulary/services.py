import logging
from datetime import date
from typing import List, Optional
from django.db import transaction
from core.integrations.dictionary import FreeDictionaryService, DatamuseService, EnglishRandomWordsService
from core.integrations.extra_apis import WordsAPIService
from .repositories import WordRepository
from .models import Word, Definition, WordOfTheDay, Bookmark, Lesson

logger = logging.getLogger(__name__)

class VocabularyService:
    def __init__(self):
        self.repository = WordRepository()
        self.dict_service = FreeDictionaryService()
        self.words_api_service = WordsAPIService()
        self.datamuse_service = DatamuseService()
        self.random_words_service = EnglishRandomWordsService()

    def get_or_fetch_word(self, word_text: str) -> Optional[Word]:
        word_text = word_text.lower()
        word = self.repository.get_by_text(word_text)

        if not word or (not word.definitions.exists() and word.phonetic is None):
            # Fetch from Free Dictionary
            definitions = self.dict_service.get_definition(word_text)
            if definitions:
                main_def = definitions[0]
                if not word:
                    word = self.repository.create(word=word_text)

                with transaction.atomic():
                    word.phonetic = next((p.text for p in main_def.phonetics if p.text), None)
                    word.audio_url = next((p.audio for p in main_def.phonetics if p.audio), None)
                    word.save()

                    # Clear old empty ones if any
                    word.definitions.all().delete()

                    for meaning in main_def.meanings:
                        for d in meaning.definitions:
                            Definition.objects.create(
                                word=word,
                                part_of_speech=meaning.part_of_speech,
                                definition_text=d
                            )
            elif not word:
                # Fallback WordsAPI or create shell
                word = self.repository.create(word=word_text)

        return word

    def get_word_of_the_day(self) -> Optional[Word]:
        today = date.today()
        wotd = WordOfTheDay.objects.filter(date=today).first()

        if not wotd:
            random_word_text = self.random_word_text = self.random_words_service.get_random_word()
            if random_word_text:
                word = self.get_or_fetch_word(random_word_text)
                if word:
                    wotd = WordOfTheDay.objects.create(word=word, date=today)

        return wotd.word if wotd else None

    def toggle_bookmark(self, user, word_id: int) -> bool:
        word = self.repository.get_by_id(word_id)
        if not word:
            return False

        bookmark, created = Bookmark.objects.get_or_create(user=user, word=word)
        if not created:
            bookmark.delete()
            return False # Unbookmarked
        return True # Bookmarked

    def get_lessons(self, level: Optional[str] = None) -> List[Lesson]:
        if level:
            return Lesson.objects.filter(level=level)
        return Lesson.objects.all()

    def get_synonyms_and_antonyms(self, word_text: str):
        return {
            "synonyms": self.datamuse_service.get_synonyms(word_text),
            "antonyms": self.datamuse_service.get_antonyms(word_text)
        }

from celery import shared_task
from .services import VocabularyService

@shared_task
def generate_word_of_the_day():
    service = VocabularyService()
    word = service.get_word_of_the_day()
    return word.word if word else None

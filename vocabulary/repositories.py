from typing import List, Optional
from .models import Word
from core.interfaces import BaseRepositoryInterface

class WordRepository(BaseRepositoryInterface[Word]):
    def get_by_id(self, id: int) -> Optional[Word]:
        try:
            return Word.objects.get(pk=id)
        except Word.DoesNotExist:
            return None

    def get_by_text(self, text: str) -> Optional[Word]:
        try:
            return Word.objects.get(word=text.lower())
        except Word.DoesNotExist:
            return None

    def list_all(self) -> List[Word]:
        return list(Word.objects.all())

    def create(self, **kwargs) -> Word:
        return Word.objects.create(**kwargs)

    def update(self, id: int, **kwargs) -> Optional[Word]:
        word = self.get_by_id(id)
        if word:
            for key, value in kwargs.items():
                setattr(word, key, value)
            word.save()
            return word
        return None

    def delete(self, id: int) -> bool:
        word = self.get_by_id(id)
        if word:
            word.delete()
            return True
        return False

    def get_or_create_by_text(self, text: str) -> Word:
        word, created = Word.objects.get_or_create(word=text.lower())
        return word

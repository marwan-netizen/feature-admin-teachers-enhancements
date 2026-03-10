from django.db import models
from django.conf import settings
from core.models import SoftDeleteModel

class Word(SoftDeleteModel):
    word = models.CharField(max_length=255, unique=True)
    phonetic = models.CharField(max_length=255, null=True, blank=True)
    audio_url = models.URLField(null=True, blank=True)
    cefr_level = models.CharField(max_length=10, null=True, blank=True) # A1, A2, B1, etc.
    frequency_score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='definitions')
    part_of_speech = models.CharField(max_length=100)
    definition_text = models.TextField()
    example_sentence = models.TextField(null=True, blank=True)

class WordOfTheDay(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    date = models.DateField(unique=True)

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='word_bookmarks')
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'word')

class Lesson(SoftDeleteModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=50)
    words = models.ManyToManyField(Word, related_name='lessons')
    created_at = models.DateTimeField(auto_now_add=True)

class UserLevel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vocabulary_level')
    current_level = models.CharField(max_length=10, default='A1')
    vocabulary_size = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

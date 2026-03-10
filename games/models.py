from django.db import models
from django.conf import settings
from vocabulary.models import Word

class FlashcardSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class GameScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=50) # 'word_race', 'sentence_match', etc.
    score = models.IntegerField()
    achieved_at = models.DateTimeField(auto_now_add=True)

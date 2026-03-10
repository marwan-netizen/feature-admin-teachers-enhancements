from django.db import models
from django.conf import settings
from vocabulary.models import Word

class ExerciseAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=100)
    score = models.FloatField()
    metadata = models.JSONField(default=dict)
    completed_at = models.DateTimeField(auto_now_add=True)

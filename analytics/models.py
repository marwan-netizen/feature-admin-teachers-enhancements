from django.db import models
from django.conf import settings

class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100) # 'dictionary_lookup', 'game_played', 'grammar_check'
    metadata = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True)

class DailyMetric(models.Model):
    date = models.DateField(unique=True)
    total_lookups = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    new_users = models.IntegerField(default=0)

from rest_framework import serializers
from .models import GameScore

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        fields = ['id', 'user', 'game_type', 'score', 'achieved_at']

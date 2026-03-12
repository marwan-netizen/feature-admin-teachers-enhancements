from rest_framework import serializers
from .models import UserActivity, DailyMetric

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['id', 'user', 'activity_type', 'metadata', 'timestamp']

class DailyMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMetric
        fields = ['date', 'total_lookups', 'total_games', 'new_users']

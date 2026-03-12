from rest_framework import serializers
from .models import MediaBookmark

class MediaBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBookmark
        fields = ['id', 'user', 'title', 'url', 'source', 'created_at']

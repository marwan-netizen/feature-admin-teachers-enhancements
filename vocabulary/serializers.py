from rest_framework import serializers
from .models import Word, Definition, Bookmark, Lesson

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ['part_of_speech', 'definition_text', 'example_sentence']

class WordSerializer(serializers.ModelSerializer):
    definitions = DefinitionSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['id', 'word', 'phonetic', 'audio_url', 'cefr_level', 'frequency_score', 'definitions']

class BookmarkSerializer(serializers.ModelSerializer):
    word_detail = WordSerializer(source='word', read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'word', 'word_detail', 'created_at']

class LessonSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'level', 'words', 'created_at']

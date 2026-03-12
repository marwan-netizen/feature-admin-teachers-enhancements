from rest_framework import serializers
from .models import Test, Question, Option, Result, Evaluation, StudentAnswer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option_id', 'option_text']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'question_type', 'difficulty_level', 'options']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['test_id', 'test_name', 'level', 'skill', 'content', 'questions']

class ResultSerializer(serializers.ModelSerializer):
    test_name = serializers.CharField(source='test.test_name', read_only=True)
    class Meta:
        model = Result
        fields = ['result_id', 'test', 'test_name', 'final_score', 'created_at']

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['answer_id', 'student', 'question', 'option', 'answer_text']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['ai_eval_id', 'answer', 'ai_score', 'ai_feedback']

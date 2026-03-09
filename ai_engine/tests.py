import pytest
from unittest.mock import MagicMock
from ai_engine.services import AIService
from testing.models import Test

@pytest.mark.django_db
class TestAIService:
    def test_generate_comprehensive_test_success(self, mocker):
        # Mock Groq Adapter
        mock_groq = mocker.patch('ai_engine.services.GroqProvider')
        mock_groq.return_value.generate.return_value = '{"reading": {"passage": "Test passage", "questions": []}, "writing": {"topic": "Test topic"}, "speaking": {"passage": "Test speaking"}}'

        service = AIService()
        test_ids = service.generate_comprehensive_test()

        assert 'reading' in test_ids
        assert 'writing' in test_ids
        assert 'speaking' in test_ids
        assert Test.objects.filter(test_id=test_ids['reading']).exists()

    def test_evaluate_response(self, mocker):
        mock_gemini = mocker.patch('ai_engine.services.GeminiProvider')
        mock_gemini.return_value.evaluate.return_value = {'score': 80, 'feedback': 'Good'}

        service = AIService()
        result = service.evaluate_response("Test text", "writing")

        assert result['score'] == 80
        assert result['feedback'] == 'Good'

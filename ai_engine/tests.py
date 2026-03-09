import pytest
from unittest.mock import MagicMock
from ai_engine.application.services import AIService
from ai_engine.domain.entities import ComprehensiveTestDTO
from ai_engine.domain.interfaces import TextGenerationProvider, EvaluationProvider

@pytest.mark.django_db
class TestAIService:
    @pytest.fixture
    def mock_text_gen(self):
        return MagicMock(spec=TextGenerationProvider)

    @pytest.fixture
    def mock_evaluator(self):
        return MagicMock(spec=EvaluationProvider)

    def test_generate_comprehensive_test_success(self, mock_text_gen, mock_evaluator):
        mock_text_gen.generate.return_value = '{"reading": {"passage": "Test passage", "questions": []}, "writing": {"topic": "Test topic"}, "speaking": {"passage": "Test speaking"}}'

        service = AIService(text_generator=mock_text_gen, evaluator=mock_evaluator)
        result = service.generate_comprehensive_test()

        assert isinstance(result, ComprehensiveTestDTO)
        assert result.reading.content == "Test passage"
        assert result.writing.content == "Test topic"
        assert result.speaking.content == "Test speaking"

    def test_evaluate_response(self, mock_text_gen, mock_evaluator):
        mock_evaluator.evaluate.return_value = {'score': 80, 'feedback': 'Good'}

        service = AIService(text_generator=mock_text_gen, evaluator=mock_evaluator)
        result = service.evaluate_response("Test text", "writing")

        assert result['score'] == 80
        assert result['feedback'] == 'Good'

import pytest
from testing.services import TestingService
from testing.models import Test, Question, Option, Result
from accounts.models import User, Student

@pytest.mark.django_db
class TestTestingService:
    @pytest.fixture
    def setup_data(self):
        user = User.objects.create(email="student@test.com", full_name="Student")
        student = Student.objects.create(user=user)
        test = Test.objects.create(test_name="Reading Test", skill="reading")
        question = Question.objects.create(test=test, question_text="Q1", question_type="mcq")
        opt1 = Option.objects.create(question=question, option_text="Correct", is_correct=True)
        opt2 = Option.objects.create(question=question, option_text="Wrong", is_correct=False)
        return user, student, test, question, opt1, opt2

    def test_process_mcq_submission(self, setup_data):
        user, student, test, question, opt1, opt2 = setup_data
        service = TestingService()

        answers = {f'q{question.question_id}': opt1.option_id}
        score = service.process_mcq_submission(user, test.test_id, student.student_id, answers, 'reading')

        assert score == 100
        assert Result.objects.filter(user=user, test=test).exists()
        assert Result.objects.get(user=user, test=test).final_score == 100

    def test_process_writing_submission(self, mocker, setup_data):
        user, student, test, _, _, _ = setup_data
        service = TestingService()

        # Mock AIService
        mocker.patch.object(service.ai_service, 'evaluate_response', return_value={'score': 90, 'feedback': 'Excellent'})

        result = service.process_writing_submission(user, test.test_id, student.student_id, "Some essay content")

        assert result['score'] == 90
        assert Result.objects.get(user=user, test=test).final_score == 90

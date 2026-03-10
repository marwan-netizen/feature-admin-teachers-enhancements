import pytest
from testing.services import TestingService
from testing.models import Test, Question, Option, Result
from accounts.models import User, Student
from ai_engine.domain.entities import ComprehensiveTestDTO, TestDTO, QuestionDTO, OptionDTO

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

        # Mock Task
        mock_task = mocker.patch('testing.tasks.evaluate_writing_submission_task.delay')
        mock_task.return_value.id = 'fake-task-id'

        task_id = service.process_writing_submission(user, test.test_id, student.student_id, "Some essay content")

        assert task_id == 'fake-task-id'

    def test_start_dynamic_test_session(self, mocker):
        service = TestingService()

        # Mock group and apply_async
        mock_group = mocker.patch('testing.services.group')
        mock_group.return_value.apply_async.return_value.id = 'fake-group-id'

        session = {}
        task_id = service.start_dynamic_test_session(session)

        assert task_id == 'fake-group-id'
        assert session['dynamic_tests_ready'] is False
        assert session['dynamic_tests_task_id'] == 'fake-group-id'

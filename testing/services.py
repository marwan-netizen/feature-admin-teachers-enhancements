"""
Application services for the Testing module.

Contains the logic for managing test sessions, persisting AI-generated tests,
and processing student submissions for all four language skills.
"""

import logging
from django.db import transaction
from .models import Test, Question, Option, StudentAnswer, Result, Evaluation
from ai_engine.application.factory import AIServiceFactory
from core.exceptions import AIServiceError
from celery import group
from .tasks import generate_comprehensive_test_task, generate_listening_test_task, evaluate_writing_submission_task

logger = logging.getLogger(__name__)

class TestingService:
    """
    Service for managing the lifecycle of English proficiency tests.
    """
    def __init__(self):
        """
        Initializes the service and its AI dependencies.
        """
        self.ai_service = AIServiceFactory.create_standard_service()

    def start_dynamic_test_session(self, session):
        """
        Asynchronously generates and prepares a dynamic test session for a student.

        Args:
            session: The Django session object to store test state.

        Returns:
            str: Task Group ID if the session was successfully started, None otherwise.
        """
        try:
            # We use a group to parallelize generation of comprehensive and listening tests
            job = group([
                generate_comprehensive_test_task.s(),
                generate_listening_test_task.s()
            ])
            result = job.apply_async()

            session['dynamic_tests_ready'] = False
            session['dynamic_tests_task_id'] = result.id
            return result.id
        except Exception as e:
            logger.error(f"Failed to start dynamic test session task: {str(e)}")
            return None

    def check_test_session_status(self, session):
        """
        Checks the status of the background generation tasks and updates session if ready.
        """
        task_id = session.get('dynamic_tests_task_id')
        if not task_id:
            return False

        from celery.result import GroupResult
        res = GroupResult.restore(task_id)
        if res and res.ready():
            results = res.get()
            # results[0] is final_ids from comprehensive task
            # results[1] is listening_id
            final_ids = results[0]
            if results[1]:
                final_ids['listening'] = results[1]

            session['dynamic_test_ids'] = final_ids
            session['dynamic_tests_ready'] = True
            return True
        return False

    def process_mcq_submission(self, user, test_id, student_id, answers_dict, skill):
        """
        Processes a multiple-choice question submission (Reading/Listening).

        Args:
            user: The User instance submitting the answers.
            test_id: ID of the test being taken.
            student_id: ID of the Student profile.
            answers_dict: Dictionary of submitted answers.
            skill: The skill being tested ('reading' or 'listening').

        Returns:
            float: The final score for this test.
        """
        test = Test.objects.get(test_id=test_id)
        questions = test.questions.all()
        correct_count = 0

        prefix = 's' if skill == 'listening' else 'q'

        with transaction.atomic():
            for question in questions:
                answer_key = f'{prefix}{question.question_id}'
                selected_option_id = answers_dict.get(answer_key)
                if selected_option_id:
                    try:
                        option = Option.objects.get(option_id=selected_option_id)
                        StudentAnswer.objects.update_or_create(
                            student_id=student_id,
                            question=question,
                            defaults={'option': option}
                        )
                        if option.is_correct:
                            correct_count += 1
                    except Option.DoesNotExist:
                        continue

            final_score = (correct_count / questions.count()) * 100 if questions.count() > 0 else 0
            Result.objects.update_or_create(
                user=user,
                test=test,
                defaults={'final_score': final_score}
            )
        return final_score

    def process_writing_submission(self, user, test_id, student_id, essay_text):
        """
        Asynchronously processes and evaluates a writing test submission.

        Args:
            user: The User instance.
            test_id: ID of the writing test.
            student_id: ID of the Student profile.
            essay_text: The student's essay content.

        Returns:
            str: Task ID of the evaluation task.
        """
        task = evaluate_writing_submission_task.delay(user.user_id, test_id, student_id, essay_text)
        return task.id

    def process_speaking_submission(self, user, test_id, student_id, transcription, accuracy):
        """
        Processes and records a speaking test submission.

        Args:
            user: The User instance.
            test_id: ID of the speaking test.
            student_id: ID of the Student profile.
            transcription: The transcribed text from the student's speech.
            accuracy: The accuracy score (0-100) provided by the client/AI.

        Returns:
            float: The accuracy score.
        """
        test = Test.objects.get(test_id=test_id)
        question, _ = Question.objects.get_or_create(
            test=test,
            defaults={'question_text': 'Speaking Passage', 'question_type': 'speaking'}
        )

        with transaction.atomic():
            answer, _ = StudentAnswer.objects.update_or_create(
                student_id=student_id,
                question=question,
                defaults={'answer_text': transcription}
            )

            Evaluation.objects.update_or_create(
                answer=answer,
                defaults={'ai_score': accuracy, 'ai_feedback': f"Accuracy: {accuracy}%"}
            )

            Result.objects.update_or_create(
                user=user,
                test=test,
                defaults={'final_score': accuracy}
            )
        return accuracy

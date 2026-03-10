"""
Celery tasks for the Testing module.
"""

import logging
from celery import shared_task
from .models import Test, Question, Option, StudentAnswer, Result, Evaluation
from ai_engine.application.factory import AIServiceFactory
from django.db import transaction
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()

def _persist_test_dto(dto):
    """
    Helper to persist a TestDTO to the database.
    """
    with transaction.atomic():
        test = Test.objects.create(
            test_name=dto.name,
            level=dto.level,
            skill=dto.skill,
            content=dto.content
        )
        for q_dto in dto.questions:
            question = Question.objects.create(
                test=test,
                question_text=q_dto.text,
                question_type=q_dto.question_type
            )
            for o_dto in q_dto.options:
                Option.objects.create(
                    question=question,
                    option_text=o_dto.text,
                    is_correct=o_dto.is_correct
                )
        return test.test_id

@shared_task(bind=True, max_retries=3)
def generate_comprehensive_test_task(self):
    """
    Task to generate comprehensive reading, writing, and speaking tests.
    """
    try:
        ai_service = AIServiceFactory.create_standard_service()
        comp_test = ai_service.generate_comprehensive_test()

        final_ids = {
            'reading': _persist_test_dto(comp_test.reading),
            'writing': _persist_test_dto(comp_test.writing),
            'speaking': _persist_test_dto(comp_test.speaking)
        }
        return final_ids
    except Exception as exc:
        logger.error(f"Error generating comprehensive test: {exc}")
        raise self.retry(exc=exc, countdown=60)

@shared_task(bind=True, max_retries=3)
def generate_listening_test_task(self):
    """
    Task to generate listening tests.
    """
    try:
        ai_service = AIServiceFactory.create_standard_service()
        listening_tests = ai_service.generate_listening_test()

        if listening_tests:
            return _persist_test_dto(listening_tests[0])
        return None
    except Exception as exc:
        logger.error(f"Error generating listening test: {exc}")
        raise self.retry(exc=exc, countdown=60)

@shared_task(bind=True, max_retries=3)
def evaluate_writing_submission_task(self, user_id, test_id, student_id, essay_text):
    """
    Task to evaluate a writing submission.
    """
    try:
        ai_service = AIServiceFactory.create_standard_service()
        test = Test.objects.get(test_id=test_id)
        question, _ = Question.objects.get_or_create(
            test=test,
            defaults={'question_text': 'Writing Essay', 'question_type': 'essay'}
        )

        evaluation = ai_service.evaluate_response(essay_text, 'writing')

        with transaction.atomic():
            answer, _ = StudentAnswer.objects.update_or_create(
                student_id=student_id,
                question=question,
                defaults={'answer_text': essay_text}
            )
            Evaluation.objects.update_or_create(
                answer=answer,
                defaults={
                    'ai_score': evaluation.get('score', 0),
                    'ai_feedback': evaluation.get('feedback', '')
                }
            )
            user = User.objects.get(user_id=user_id)
            Result.objects.update_or_create(
                user=user,
                test=test,
                defaults={'final_score': evaluation.get('score', 0)}
            )
        return evaluation
    except Exception as exc:
        logger.error(f"Error evaluating writing submission: {exc}")
        raise self.retry(exc=exc, countdown=60)

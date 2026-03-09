import logging
from django.db import transaction
from .models import Test, Question, Option, StudentAnswer, Result, Evaluation
from ai_engine.application.factory import AIServiceFactory
from core.exceptions import AIServiceError

logger = logging.getLogger(__name__)

class TestingService:
    def __init__(self):
        self.ai_service = AIServiceFactory.create_standard_service()

    def _persist_test_dto(self, dto):
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

    def start_dynamic_test_session(self, session):
        try:
            comp_test = self.ai_service.generate_comprehensive_test()
            listening_tests = self.ai_service.generate_listening_test()

            session['dynamic_tests_ready'] = True
            final_ids = {}

            final_ids['reading'] = self._persist_test_dto(comp_test.reading)
            final_ids['writing'] = self._persist_test_dto(comp_test.writing)
            final_ids['speaking'] = self._persist_test_dto(comp_test.speaking)

            if listening_tests:
                first_listening_id = self._persist_test_dto(listening_tests[0])
                final_ids['listening'] = first_listening_id

            session['dynamic_test_ids'] = final_ids
            return True
        except AIServiceError as e:
            logger.error(f"Failed to start dynamic test session: {str(e)}")
            return False

    def process_mcq_submission(self, user, test_id, student_id, answers_dict, skill):
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
        test = Test.objects.get(test_id=test_id)
        question, _ = Question.objects.get_or_create(
            test=test,
            defaults={'question_text': 'Writing Essay', 'question_type': 'essay'}
        )

        try:
            evaluation = self.ai_service.evaluate_response(essay_text, 'writing')
        except AIServiceError as e:
            logger.error(f"Evaluation failed in TestingService: {str(e)}")
            evaluation = {'score': 0, 'feedback': 'Evaluation failed.'}

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
            Result.objects.update_or_create(
                user=user,
                test=test,
                defaults={'final_score': evaluation.get('score', 0)}
            )
        return evaluation

    def process_speaking_submission(self, user, test_id, student_id, transcription, accuracy):
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

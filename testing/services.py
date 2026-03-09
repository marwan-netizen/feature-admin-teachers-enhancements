import logging
from django.db import transaction
from .models import Test, Question, Option, StudentAnswer, Result, Evaluation
from ai_engine.services import AIService

logger = logging.getLogger(__name__)

class TestingService:
    def __init__(self):
        self.ai_service = AIService()

    def start_dynamic_test_session(self, session):
        test_ids = self.ai_service.generate_comprehensive_test()
        listening_id = self.ai_service.generate_listening_test()

        if test_ids or listening_id:
            session['dynamic_tests_ready'] = True
            final_ids = test_ids or {}
            if listening_id:
                final_ids['listening'] = listening_id
            session['dynamic_test_ids'] = final_ids
            return True
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

        evaluation = self.ai_service.evaluate_response(essay_text, 'writing')

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

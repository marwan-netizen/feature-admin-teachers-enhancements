from typing import List, Dict
from assessment.models import ExerciseAttempt
from .models import AdaptivePlan

class AdaptiveLearningService:
    def generate_adaptive_plan(self, user) -> AdaptivePlan:
        # Simple adaptive logic: find exercises with low scores
        low_scores = ExerciseAttempt.objects.filter(user=user, score__lt=0.7).values('exercise_type').distinct()

        plan_content = {
            "focus_exercises": [item['exercise_type'] for item in low_scores],
            "recommendations": ["Review bookmarked words", "Daily pronunciation practice"],
            "next_goal": "Reach 80% accuracy in Sentence Completion"
        }

        return AdaptivePlan.objects.create(
            user=user,
            plan_name=f"Personalized Plan - {user.username}",
            content=plan_content
        )

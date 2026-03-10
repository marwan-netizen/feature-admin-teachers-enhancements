import logging
from typing import List, Dict
from collections import Counter
from core.integrations.analysis_media import LanguageToolService
from vocabulary.models import Word, UserLevel
from .models import LearningGap, TrainingPlan

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.lt_service = LanguageToolService()

    def analyze_grammar(self, text: str):
        return self.lt_service.check_text(text)

    def analyze_vocabulary_diversity(self, text: str) -> Dict:
        words = text.lower().split()
        if not words: return {"ttr": 0, "unique": 0, "total": 0}

        unique_words = set(words)
        ttr = len(unique_words) / len(words) # Type-Token Ratio

        return {
            "ttr": round(ttr, 3),
            "unique": len(unique_words),
            "total": len(words),
            "diversity_score": round(ttr * 100, 1)
        }

    def detect_cefr_level(self, vocabulary: List[str]) -> str:
        # Improved mock CEFR detection
        count = len(vocabulary)
        if count < 50: return 'A1'
        if count < 150: return 'A2'
        if count < 300: return 'B1'
        if count < 600: return 'B2'
        if count < 1200: return 'C1'
        return 'C2'

    def detect_learning_gaps(self, user_answers: List[Dict]) -> List[str]:
        topic_errors = Counter()
        topic_total = Counter()

        for ans in user_answers:
            topic_total[ans['topic']] += 1
            if not ans.get('is_correct', False):
                topic_errors[ans['topic']] += 1

        gaps = []
        for topic in topic_total:
            if topic_errors[topic] / topic_total[topic] > 0.3:
                gaps.append(topic)
        return gaps

    def generate_training_plan(self, user) -> TrainingPlan:
        # Better training plan generation
        gaps = LearningGap.objects.filter(user=user, resolved_at__isnull=True)
        focus_areas = [gap.topic for gap in gaps] if gaps.exists() else ["General Vocabulary", "Basic Grammar"]

        plan_data = {
            "focus_areas": focus_areas,
            "recommended_lessons": ["Intermediate Grammar", "Advanced Reading"] if "Grammar" in str(focus_areas) else ["Daily Vocabulary"],
            "daily_goal": "25 minutes",
            "weekly_target": "5 lessons completed"
        }
        return TrainingPlan.objects.create(user=user, plan_content=plan_data)

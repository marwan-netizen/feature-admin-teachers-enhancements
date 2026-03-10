import random
import logging
from typing import List, Dict
from vocabulary.models import Word, Definition
from core.integrations.analysis_media import ConceptNetService

logger = logging.getLogger(__name__)

class GamesService:
    def __init__(self):
        self.conceptnet = ConceptNetService()

    def get_flashcards(self, user, count: int = 10) -> List[Dict]:
        # Preference to bookmarked words
        words = list(Word.objects.filter(word_bookmarks__user=user)[:count])
        if len(words) < count:
            remaining = count - len(words)
            extra_words = list(Word.objects.exclude(word_bookmarks__user=user).order_by('?')[:remaining])
            words.extend(extra_words)

        cards = []
        for word in words:
            cards.append({
                'id': word.id,
                'word': word.word,
                'phonetic': word.phonetic,
                'definition': word.definitions.first().definition_text if word.definitions.exists() else "No definition available."
            })
        return cards

    def get_sentence_completion_data(self, count: int = 5) -> List[Dict]:
        definitions = list(Definition.objects.exclude(example_sentence__isnull=True).exclude(example_sentence="")[:count])
        exercises = []
        for d in definitions:
            sentence = d.example_sentence
            word_text = d.word.word
            masked_sentence = sentence.replace(word_text, "_______")
            masked_sentence = masked_sentence.replace(word_text.capitalize(), "_______")

            # Distractors
            distractors = list(Word.objects.exclude(id=d.word.id).order_by('?')[:3].values_list('word', flat=True))
            options = distractors + [word_text]
            random.shuffle(options)

            exercises.append({
                'sentence': masked_sentence,
                'correct_answer': word_text,
                'options': options
            })
        return exercises

    def get_word_network(self, word_text: str):
        edges = self.conceptnet.get_related_terms(word_text)
        nodes = [{'id': word_text, 'group': 1}]
        links = []

        seen_words = {word_text}
        for edge in edges[:15]:
            start = edge['start']['label']
            end = edge['end']['label']
            rel = edge['rel']['label']

            other = end if start.lower() == word_text.lower() else start
            if other.lower() not in seen_words:
                nodes.append({'id': other, 'group': 2})
                seen_words.add(other.lower())

            links.append({'source': start, 'target': end, 'value': 1, 'relation': rel})

        return {'nodes': nodes, 'links': links}

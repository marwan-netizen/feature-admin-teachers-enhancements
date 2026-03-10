from django.shortcuts import render
from django.views import View
from .services import AnalysisService

class GrammarTrainerView(View):
    def get(self, request):
        return render(request, 'grammar_analysis/trainer.html')

    def post(self, request):
        text = request.POST.get('text', '')
        service = AnalysisService()
        analysis = service.analyze_grammar(text)
        return render(request, 'grammar_analysis/trainer.html', {
            'text': text,
            'analysis': analysis
        })

class CEFRDetectionView(View):
    def get(self, request):
        # In a real app, we'd fetch the user's known words
        known_words = ['hello', 'world', 'education', 'complex', 'infrastructure']
        service = AnalysisService()
        level = service.detect_cefr_level(known_words)
        return render(request, 'grammar_analysis/cefr.html', {'level': level})

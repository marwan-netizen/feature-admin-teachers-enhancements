from django.shortcuts import render
from enterprise.ai.agents import get_ai_insights
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def ai_insights_view(request):
    """
    Dedicated view for AI-generated operational insights.
    """
    insights = get_ai_insights()
    return render(request, 'admin/enterprise/ai_insights.html', {
        'insights': insights,
        'title': 'AI Operational Intelligence'
    })

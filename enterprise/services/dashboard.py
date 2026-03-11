from enterprise.ai.agents import get_ai_insights
from enterprise.devops.metrics import get_system_metrics

def get_dashboard_data(request):
    insights = get_ai_insights()
    system_metrics = get_system_metrics()
    return {
        "ai_insights": insights,
        "system_metrics": system_metrics,
        "metrics": {
            "active_users": 150,  # Example static metrics for now
            "total_tests": 45,
            "system_health": "Healthy",
        }
    }

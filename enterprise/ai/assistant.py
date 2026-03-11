from ai_engine.application.factory import AIServiceFactory
from enterprise.devops.metrics import get_system_metrics
from core.models import ActivityLog

class DataAssistant:
    """
    Natural Language Interface for System Data and Operations.
    """
    def __init__(self):
        self.ai_service = AIServiceFactory.create_standard_service()

    def query(self, user_query):
        """
        Translates natural language to system insights or data summaries.
        """
        context = {
            'metrics': get_system_metrics(),
            'recent_logs': list(ActivityLog.objects.all().values()[:5])
        }
        # In a real implementation, this would call the LLM to process the query
        # using the provided system context.
        return {
            'answer': f"Processed query: {user_query}",
            'context_used': context,
            'visualization': 'table'
        }

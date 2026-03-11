import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from enterprise.devops.metrics import SystemHealthService
from enterprise.ai.agents import get_ai_insights

User = get_user_model()

@pytest.mark.django_db
class TestMissionControl:
    def test_system_health_service(self):
        report = SystemHealthService.get_full_report()
        assert 'metrics' in report
        assert 'status' in report
        assert report['metrics']['cpu_usage'] >= 0

    def test_ai_insights_generation(self):
        insights = get_ai_insights()
        assert len(insights) > 0
        assert 'insight' in insights[0]
        assert 'confidence' in insights[0]

    def test_audit_log_view_accessible_by_staff(self, client):
        admin_user = User.objects.create_superuser(email='admin@test.com', full_name='Admin', password='password')
        client.force_login(admin_user)
        url = reverse('admin_audit_logs')
        response = client.get(url)
        assert response.status_code == 200

    def test_health_view_accessible_by_staff(self, client):
        admin_user = User.objects.create_superuser(email='admin2@test.com', full_name='Admin 2', password='password')
        client.force_login(admin_user)
        url = reverse('admin_system_health')
        response = client.get(url)
        assert response.status_code == 200

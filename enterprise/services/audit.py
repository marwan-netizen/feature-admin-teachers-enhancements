from django.shortcuts import render
from core.models import ActivityLog
from simple_history.models import HistoricalRecords
from django.contrib.admin.views.decorators import staff_member_required
from django.db import models

@staff_member_required
def audit_log_view(request):
    """
    Unified view for analyzing security events and data changes.
    """
    logs = ActivityLog.objects.all().order_by('-created_at')[:100]
    return render(request, 'admin/enterprise/audit_logs.html', {
        'logs': logs,
        'title': 'Security & Data Audit'
    })

def analyze_anomalies():
    """
    AI-driven anomaly detection in audit logs.
    """
    suspicious_ips = ActivityLog.objects.filter(action='failed_login').values('ip_address').annotate(count=models.Count('id')).filter(count__gt=10)
    anomalies = []
    for entry in suspicious_ips:
        anomalies.append({
            'type': 'Brute Force Attempt',
            'ip': entry['ip_address'],
            'count': entry['count']
        })
    return anomalies

from django.shortcuts import render
from enterprise.devops.metrics import SystemHealthService
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def diagnostic_center_view(request):
    """
    On-demand system diagnostics and health checks.
    """
    report = SystemHealthService.get_full_report()
    return render(request, 'admin/enterprise/diagnostics.html', {
        'report': report,
        'title': 'Engineering Diagnostics'
    })

def run_db_diagnostic():
    # Logic to check DB latency and connection pool
    pass

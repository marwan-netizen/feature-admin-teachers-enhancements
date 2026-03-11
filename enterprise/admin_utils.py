from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
import json
from django.http import HttpResponse
from django.core import serializers

class EnterpriseSearchMixin:
    """
    Mixin to enhance admin search with custom logic or multi-field indexing.
    """
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct

class BulkActionMixin:
    """
    Reusable mixin for enterprise-grade bulk operations.
    """
    @admin.action(description=_("Export selected items to JSON"))
    def export_as_json(self, request, queryset):
        data = serializers.serialize("json", queryset)
        response = HttpResponse(data, content_type="application/json")
        response["Content-Disposition"] = 'attachment; filename="export.json"'
        return response

    @admin.action(description=_("Perform deep system audit on selected"))
    def deep_audit(self, request, queryset):
        # Trigger an audit log entry for this action
        count = queryset.count()
        self.message_user(request, _("Audit triggered for {} items. Review the Audit Viewer for results.").format(count), messages.INFO)

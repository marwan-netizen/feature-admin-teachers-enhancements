from rest_framework import viewsets, permissions
from .models import UserActivity, DailyMetric
from .serializers import ActivitySerializer, DailyMetricSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return UserActivity.objects.all()
        return UserActivity.objects.filter(user=self.request.user)

class AdminMetricViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DailyMetric.objects.all()
    serializer_class = DailyMetricSerializer
    permission_classes = [permissions.IsAdminUser]

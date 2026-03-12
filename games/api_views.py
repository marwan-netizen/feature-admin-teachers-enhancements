from rest_framework import viewsets, permissions
from .models import GameScore
from .serializers import GameScoreSerializer

class GameScoreViewSet(viewsets.ModelViewSet):
    serializer_class = GameScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GameScore.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

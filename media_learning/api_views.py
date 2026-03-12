from rest_framework import viewsets, permissions
from .models import MediaBookmark
from .serializers import MediaBookmarkSerializer

class MediaBookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = MediaBookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MediaBookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

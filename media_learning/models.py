from django.db import models
from django.conf import settings

class MediaBookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    source = models.CharField(max_length=50) # 'wikipedia', 'podcast', etc.
    created_at = models.DateTimeField(auto_now_add=True)

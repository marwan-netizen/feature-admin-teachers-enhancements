"""
Database models for the AI Engine module.
"""

from django.db import models
from accounts.models import User
from core.models import SoftDeleteModel

class ChatSession(SoftDeleteModel):
    """
    Model representing a message in an AI chatbot session.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50) # 'user' or 'model'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'chat_sessions'

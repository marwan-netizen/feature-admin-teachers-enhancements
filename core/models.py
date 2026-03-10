"""
Core database models and common base classes.

Contains foundational components like SoftDelete logic, activity logging,
and global notification models.
"""

from django.db import models
from django.utils import timezone
from django.db import transaction

class SoftDeleteManager(models.Manager):
    """
    Manager that filters out soft-deleted records by default.
    """
    def get_queryset(self):
        """
        Returns a queryset excluding deleted records.
        """
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    """
    Abstract base class for models that support soft deletion.
    """
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        """
        Performs a soft delete by setting the deleted_at timestamp.
        """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """
        Restores a soft-deleted record.
        """
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True

class ActivityLog(models.Model):
    """
    Global log for tracking user actions and data changes.
    """
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=30)
    model_type = models.CharField(max_length=100)
    model_id = models.BigIntegerField(null=True, blank=True)
    model_label = models.CharField(max_length=255, null=True, blank=True)
    old_values = models.JSONField(null=True, blank=True)
    new_values = models.JSONField(null=True, blank=True)
    changed_fields = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activity_log'

class Notification(models.Model):
    """
    System for platform-wide and user-specific notifications.
    """
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.BigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notifications'

import base64
from django.db import models
from core.kms import kms_manager

class EncryptedField(models.CharField):
    """
    Custom Django field that automatically encrypts and decrypts data
    using the KMS Manager.
    """
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            return kms_manager.decrypt(value)
        except Exception:
            return value # Fallback for unencrypted data during migration

    def to_python(self, value):
        if value is None:
            return value
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return kms_manager.encrypt(str(value))

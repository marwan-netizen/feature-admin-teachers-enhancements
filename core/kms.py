import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from django.conf import settings

class KMSManager:
    """
    Portable KMS Manager.
    In production, this should interface with HashiCorp Vault or AWS KMS.
    For this implementation, it uses a Master Key from environment variables.
    """
    def __init__(self):
        self.master_key = os.environ.get('KMS_MASTER_KEY')
        if not self.master_key:
            # Fallback for development, but should raise error in production
            self.master_key = base64.urlsafe_b64encode(b'32_byte_fallback_key_for_dev_only').decode()

    def encrypt(self, data: str) -> str:
        aesgcm = AESGCM(base64.urlsafe_b64decode(self.master_key))
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data.encode(), None)
        return base64.b64encode(nonce + ciphertext).decode()

    def decrypt(self, encrypted_data: str) -> str:
        raw_data = base64.b64decode(encrypted_data)
        nonce = raw_data[:12]
        ciphertext = raw_data[12:]
        aesgcm = AESGCM(base64.urlsafe_b64decode(self.master_key))
        decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted_data.decode()

kms_manager = KMSManager()

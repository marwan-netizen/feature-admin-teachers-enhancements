from django.test import TestCase
from django.contrib.auth import get_user_model
from core.kms import kms_manager
from core.fields import EncryptedField

User = get_user_model()

class SecurityTest(TestCase):
    def test_password_hashing_is_argon2(self):
        user = User.objects.create_user(email='test@example.com', full_name='Test', password='SecurePassword123!')
        self.assertTrue(user.password.startswith('argon2'))

    def test_kms_encryption_decryption(self):
        original_text = "Sensitive data"
        encrypted = kms_manager.encrypt(original_text)
        decrypted = kms_manager.decrypt(encrypted)
        self.assertEqual(original_text, decrypted)
        self.assertNotEqual(original_text, encrypted)

    def test_encrypted_field_integration(self):
        # This tests if the EncryptedField logic is sound
        field = EncryptedField()
        val = "Super secret"
        prep_val = field.get_prep_value(val)
        self.assertNotEqual(val, prep_val)
        decrypted = field.from_db_value(prep_val, None, None)
        self.assertEqual(val, decrypted)

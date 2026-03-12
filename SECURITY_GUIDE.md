# Security Guide for Developers

## 1. Authentication & MFA
- Always use `accounts.User` for authentication.
- Users can enable MFA via the profile settings (using TOTP).
- Admin access requires MFA to be enabled in production.

## 2. Authorization (RBAC)
- Use `@role_required('admin')` or check `request.user.role`.
- Use Django Guardian for object-level permissions.

## 3. Data Protection
- Use `EncryptedField` for sensitive data in models:
  ```python
  from core.fields import EncryptedField
  class SecretData(models.Model):
      content = EncryptedField(max_length=255)
  ```

## 4. Input Sanitization
- Always use `sanitize_input()` from `core.utils` when handling raw HTML or user-provided data that will be rendered outside of standard Django templates.

## 5. Security Scanning
- Run `bandit -r .` and `safety check -r requirements.txt` before every commit.
- Ensure all dependencies are pinned.

import re
from django.core.exceptions import ValidationError

def validate_secure_password(password):
    """
    Validates that a password meets complexity requirements.
    """
    if len(password) < 12:
        raise ValidationError("Password must be at least 12 characters long.")
    if not re.search("[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search("[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search("[0-9]", password):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must contain at least one special character.")

def sanitize_input(text):
    """
    Basic input sanitization to prevent XSS.
    In Django, templates auto-escape, but this is for manual cleaning.
    """
    if not isinstance(text, str):
        return text
    # Basic HTML escaping
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

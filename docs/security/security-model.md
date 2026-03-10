# Security Model

Security is a top priority for LingoPulse AI. The platform implements several layers of protection to ensure user data and system integrity.

## 🛡 Authentication & Authorization

- **Session Security**: Cookies are flagged as `HttpOnly` and `Secure` (in production) to prevent XSS-based session theft.
- **RBAC (Role-Based Access Control)**: Strictly enforced at the view level using Django's `user_passes_test` or custom decorators.
- **Password Hashing**: Uses Django's default PBKDF2 algorithm with a high iteration count.

## 🔒 Data Protection

- **Soft Delete**: Prevents accidental data loss by marking records as deleted instead of removing them from the DB.
- **SQL Injection**: Prevented by using Django's ORM for all database interactions.
- **XSS Protection**: Django's template engine automatically escapes all variables.
- **CSRF Protection**: Enforced on all state-changing operations.

## 🤖 AI Safety & Privacy

- **Input Sanitization**: All student inputs are sanitized before being sent to external AI providers.
- **Provider Isolation**: AI providers only receive the minimal data necessary for their specific task (e.g., an essay text for grading, not user profile details).
- **Rate Limiting**: Implemented to prevent abuse of expensive AI API endpoints.

## 📡 Infrastructure Security

- **SSL/TLS**: All production traffic is encrypted using Let's Encrypt certificates.
- **Environment Variables**: Sensitive keys (API keys, DB passwords) are never committed to the repository and are managed via `.env` files or secret managers.

# Threat Model - LingoPulse AI

## 1. System Overview
LingoPulse AI is a modular English proficiency platform. It processes sensitive Personal Identifiable Information (PII), academic records, and interfaces with multiple external AI providers.

## 2. Trust Boundaries
- **External Boundary**: Between the public internet and the Django web server.
- **Service Boundary**: Between the Django application and internal services (Postgres, Redis).
- **Provider Boundary**: Between the application and external AI APIs (Groq, Gemini).

## 3. Critical Assets
- User Credentials (Hashed)
- Student Performance Data
- Financial/Payment Records (if applicable)
- Health-related profile data
- AI Provider API Keys

## 4. STRIDE Analysis

| Threat Type | Threat Description | Mitigation Strategy |
|-------------|--------------------|---------------------|
| **Spoofing** | Attackers impersonating students or admins. | Enforce MFA (TOTP) and strong password policies (Argon2id). |
| **Tampering** | Modification of test results or profile data. | Implement HMAC-SHA256 signatures for critical data and strict RBAC. |
| **Repudiation** | Users denying they took a test or accessed data. | Implement tamper-proof audit logging (Enterprise Audit module). |
| **Information Disclosure** | Leakage of PII or AI API keys. | Field-level encryption (AES-256-GCM) and HashiCorp Vault. |
| **Denial of Service** | Resource exhaustion via excessive AI requests. | Rate limiting at Nginx and Django levels (RatelimitMiddleware). |
| **Elevation of Privilege** | Student accessing Admin or Teacher functions. | Strict Object-level permissions (Django Guardian) and RBAC. |

## 5. Attack Surface
- /admin/ interface
- API endpoints for test generation
- User profile upload (Media storage)
- Password reset flows

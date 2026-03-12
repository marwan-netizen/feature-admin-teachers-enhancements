# LingoPulse AI - Architecture Overview

LingoPulse AI follows a **Modular Monolith** architecture with **Clean Architecture** principles within each module. This ensures separation of concerns, high testability, and ease of maintenance.

## Architecture Layers

### 1. Domain Layer (`models.py`)
- Contains Django models that represent the core entities of the system.
- Includes `SoftDeleteModel` for safe data management.
- Minimal logic is kept in this layer.

### 2. Application Layer (`services.py`)
- Orchestrates the business logic of the application.
- Decoupled from HTTP requests and specific infrastructure details.
- Each app (e.g., `testing`, `classroom`) has its own `services.py`.

### 3. Interface Layer (`views.py`)
- Handles HTTP requests and responses.
- Delegates business logic to the Application Layer.
- "Thin" views focused only on request parsing and result presentation.

### 4. Infrastructure Layer (`adapters/`)
- Concrete implementations of external services.
- Primarily used in the `ai_engine` app to abstract different AI providers (Groq, Gemini, OpenRouter).
- Interfaces (Ports) are defined in `interfaces/base.py`.

## Key Modules

### AI Engine (`ai_engine`)
- **Adapters**: Concrete classes for each AI provider.
- **Interfaces**: ABCs defining the contracts for AI operations.
- **AIService**: High-level service for test generation and evaluation.

### Testing (`testing`)
- **TestingService**: Manages the flow of dynamic English proficiency tests.

### Classroom (`classroom`)
- **ClassroomService**: Manages classes, assignments, and online sessions.

## Infrastructure Improvements
- **Global Error Handling**: Middleware catches unhandled exceptions and logs them in a structured JSON format.
- **Health Checks**: A `/health/` endpoint provides status monitoring.
- **Soft Deletes**: Implemented across all major models to prevent accidental data loss.

## Security Architecture (Added)
- **KMS & Field Encryption**: Implemented AES-256-GCM field-level encryption for PII.
- **Identity & MFA**: Enforced Argon2id and integrated TOTP-based MFA.
- **Network Segmentation**: Internal Docker network isolation for databases.
- **Secure CI/CD**: Automated SAST and secret scanning integrated into GitHub Actions.
- **Threat Model**: Based on STRIDE methodology to mitigate Spoofing, Tampering, and Information Disclosure.

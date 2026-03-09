# LingoPulse AI - Developer Guide

## Architecture Summary
LingoPulse AI uses a **Modular Clean Architecture**. This ensures that the core business logic (Domain/Application) is isolated from infrastructure details (Database, AI APIs).

### Layers
1.  **Domain:** Core logic, entities (DTOs), and interfaces.
2.  **Application:** Services and Use Cases.
3.  **Infrastructure:** Concrete implementations (Django ORM, AI Adapters).
4.  **Interface:** Views, URLs, and CLI.

## Module: AI Engine
The AI Engine is responsible for test generation and evaluation. It follows strict dependency inversion.

### Key Components
- `AIService`: The main orchestrator.
- `AIServiceFactory`: Responsible for injecting concrete providers.
- `domain.interfaces`: Definitions for AI providers.

## Module: Testing
The Testing module manages proficiency tests and user results. It consumes DTOs from the AI Engine.

## Running Tests
Ensure `APP_KEY` is set:
```bash
APP_KEY=secret python -m pytest
```

## Creating New AI Providers
1.  Implement the relevant interface in `ai_engine.domain.interfaces`.
2.  Add the concrete implementation in `ai_engine.infrastructure.adapters`.
3.  Update the `AIServiceFactory` to use the new provider.

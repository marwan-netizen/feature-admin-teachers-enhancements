# Target Architecture Design: Modular Clean Architecture

## 1. Overview
The target architecture for LingoPulse AI is a **Modular Clean Architecture**. This approach combines the modularity of a monolith with the strict layering of Clean Architecture (Hexagonal Architecture).

## 2. Layer Definitions

### 2.1 Domain Layer (The Core)
- **Entities:** Pure Python classes (Dataclasses) representing domain concepts.
- **Interfaces (Ports):** Abstract definitions of external requirements (e.g., `TextGenerationProvider`).
- **Exceptions:** Domain-specific error types.

### 2.2 Application Layer (Use Cases)
- **Services:** Orchestrate domain logic.
- **Rules:** No knowledge of HTTP or specific database implementation.

### 2.3 Infrastructure Layer (Adapters)
- **Repositories:** Concrete implementation of data persistence (Django ORM).
- **External Adapters:** Implementation of AI providers (Groq, Gemini).
- **Configuration:** Environment handling.

### 2.4 Interface Layer (The Edge)
- **Web:** Django Views, Serializers.
- **CLI:** Management commands.

## 3. Communication Patterns
- **Inward Dependency:** Dependencies always point toward the Domain Layer.
- **DTOs:** Communication between modules and layers occurs via Data Transfer Objects.
- **Dependency Injection:** Infrastructure components are injected into the Application layer.

## 4. Proposed Folder Structure
```text
app/
├── core/               # Shared utilities, base exceptions, base models
├── [module]/           # e.g., ai_engine, testing, accounts
│   ├── domain/         # Entities, Interface definitions
│   ├── application/    # Services, Use Case logic
│   ├── infrastructure/ # Concrete adapters, repositories
│   └── interface/      # Views, Serializers, URLs
└── lingopulse/         # Project root configuration
```

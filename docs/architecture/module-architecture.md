# Module Architecture

Each module (Django app) in LingoPulse AI is structured to enforce separation of concerns.

## 📁 Standard Module Structure

```text
module_name/
├── domain/             # Entities and Interfaces (Ports)
│   ├── entities.py     # Data Transfer Objects (DTOs)
│   └── interfaces.py   # Abstract Base Classes (ABCs)
├── application/        # Business Logic (Use Cases)
│   ├── services.py     # Orchestration and logic
│   └── factory.py      # Dependency injection/instantiation
├── infrastructure/     # External Implementations (Adapters)
│   └── adapters/       # Concrete providers (APIs, DB, etc.)
├── migrations/         # Django DB migrations
├── templates/          # Module-specific UI
├── models.py           # Persistence layer (Domain Models)
├── views.py            # HTTP Interface (Controllers)
└── urls.py             # Route definitions
```

## 🧩 Key Modules

### 1. `ai_engine`
The most complex module, implementing the Port/Adapter pattern for AI services.
- **Ports**: `TextGenerationProvider`, `EvaluationProvider`, `TTSProvider`.
- **Adapters**: `GroqProvider`, `GeminiProvider`, `OpenRouterProvider`.

### 2. `testing`
Manages the lifecycle of language proficiency tests.
- Coordinates between `ai_engine` for test generation/grading and its own persistence layer.

### 3. `classroom`
Handles the academic structure of the platform.
- Manages Classes, Assignments, and Online Sessions (Jitsi).

### 4. `accounts`
Extends the default Django auth system.
- Defines a custom `User` model and specific profiles for `Student`, `Teacher`, and `Admin`.

### 5. `core`
Provides foundational functionality.
- **Soft Delete**: Base model for safe data deletion.
- **Global Error Handling**: Middleware for consistent API/UI error responses.
- **Activity Logging**: Tracks user actions across the system.

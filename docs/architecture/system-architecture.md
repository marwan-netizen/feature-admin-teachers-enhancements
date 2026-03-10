# System Architecture

LingoPulse AI is designed as a **Modular Monolith** following **Clean Architecture** (Hexagonal) principles. This approach allows for a highly decoupled system where business logic is isolated from external infrastructure and UI concerns.

## 🏛 Architectural Principles

1.  **Separation of Concerns**: Each module (App) is responsible for a specific domain.
2.  **Dependency Inversion**: High-level modules do not depend on low-level modules. Both depend on abstractions (Interfaces/Ports).
3.  **Encapsulation**: Business logic is contained within Service layers, keeping Views "thin".
4.  **Single Source of Truth**: Data models are defined in the Domain layer and shared across the module.

## 🏗 High-Level Components

-   **Modular Apps**: Individual Django apps (`accounts`, `testing`, `classroom`, `ai_engine`, `core`) representing distinct domains.
-   **AI Integration Layer**: A specialized module (`ai_engine`) that abstracts various AI providers behind a unified interface.
-   **Common Core**: Shared utilities, middleware, and base models (`core`) used across the entire system.
-   **Client Layer**: Django templates enhanced with modern CSS (Tailwind) and JS (Vite pipeline).

## 🔄 Data Flow

1.  **Request**: A user makes an HTTP request which is caught by the Django URL dispatcher.
2.  **View (Interface Layer)**: The view parses the request and calls the appropriate method in the **Service Layer**.
3.  **Service (Application Layer)**: The service orchestrates business logic. It may interact with the **Domain Layer** (Models) or call the **AI Engine** via interfaces.
4.  **Infrastructure Layer**: Concrete implementations (Adapters) like `GroqProvider` or `GeminiProvider` handle communication with external APIs.
5.  **Response**: The service returns data to the view, which renders a template or returns a JSON response.

## 🗄 Storage Architecture

-   **Primary Database**: RDBMS (SQLite/PostgreSQL) stores structured data (Users, Tests, Results, Sessions).
-   **Media Storage**: Filesystem (local or S3-compatible) stores student submissions and AI-generated audio files.
-   **Session Storage**: Django session framework handles user authentication and transient test state.

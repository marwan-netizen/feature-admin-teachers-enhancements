# ADR 2: Dependency Inversion in AI Engine

## Context
The `AIService` directly instantiated concrete adapters (e.g., `GroqProvider`), making it difficult to swap providers or mock them during unit testing.

## Decision
We implemented Dependency Inversion by requiring `AIService` to accept interface-typed providers in its constructor. A `AIServiceFactory` was introduced to manage the instantiation of concrete classes.

## Consequences
- **Positive:** `AIService` is now decoupled from specific AI vendors. Unit tests can now use pure mocks without monkey-patching imports.
- **Positive:** Easier to implement multi-provider strategies or fallback mechanisms in the future.

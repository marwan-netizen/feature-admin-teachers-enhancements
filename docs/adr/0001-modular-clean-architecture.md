# ADR 1: Adoption of Modular Clean Architecture

## Context
The project was originally structured as a standard Django monolith with tightly coupled apps. Specifically, the `ai_engine` and `testing` apps had circular dependencies and leaky abstractions.

## Decision
We decided to refactor the project into a Modular Clean Architecture. Each module (app) is now divided into Domain, Application, Infrastructure, and Interface layers.

## Consequences
- **Positive:** Improved testability, clear module boundaries, and elimination of circular dependencies.
- **Negative:** Increased boilerplate (DTOs, interfaces) and initial refactoring overhead.

# ADR 3: Data Transfer Objects (DTOs) for Cross-Module Communication

## Context
Modules were communicating by passing Django Model instances, which forced modules to import each other's models, leading to tight coupling and circular dependencies.

## Decision
We introduced DTOs (Data Transfer Objects) as the primary medium for cross-module communication. `AIService` now returns DTOs, and the `testing` module is responsible for persisting these to its own database tables.

## Consequences
- **Positive:** Broken circular dependencies.
- **Positive:** Explicit contracts between modules.
- **Negative:** Requires manual mapping between DTOs and Django Models.

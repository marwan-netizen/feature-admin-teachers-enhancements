# Testing Strategy

LingoPulse AI employs a multi-layered testing strategy to ensure reliability and correctness across its complex AI integrations.

## 🧪 Testing Layers

### 1. Unit Tests
-   Located alongside the code (e.g., `testing/tests.py`).
-   Focus on individual services and logic components.
-   External AI services are mocked to ensure fast, deterministic tests.

### 2. Integration Tests
-   Verify interaction between modules (e.g., `TestingService` interacting with `AIService`).
-   Uses Django's `TestCase` with a test database.

### 3. End-to-End (E2E) Tests
-   Located in `tests/selenium/`.
-   Uses Selenium and the Page Object Model (POM).
-   Simulates real user workflows (Registration -> Taking a Test -> Viewing Results).
-   Supports multiple browsers (Chrome, Firefox, Edge).

## 🚀 Running Tests

### Standard Pytest
```bash
APP_KEY=secret python -m pytest
```

### E2E Selenium Tests
```bash
# Ensure browser drivers are installed
cd tests/selenium
pytest tests/
```

## 🛠 Mocking AI Services

Since AI API calls are expensive and slow, we use mock adapters during development and testing.
- See `ai_engine/tests.py` for examples of how to mock `GroqProvider` and `GeminiProvider`.

## 📊 Coverage

We aim for high test coverage, especially in the `application` (Service) layers of each module.

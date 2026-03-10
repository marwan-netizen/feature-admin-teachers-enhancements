# Developer Guide

This guide is intended for developers who wish to contribute to or maintain LingoPulse AI.

## 🛠 Project Structure

LingoPulse AI follows a modular clean architecture. For an overview of the directory structure and design philosophy, see the [Module Architecture](../architecture/module-architecture.md).

## 💻 Local Development Workflow

1.  **Branching**: Create a new branch for every feature or bug fix: `git checkout -b feature/your-feature-name`.
2.  **Environment**: Ensure your `.env` file is correctly configured with required API keys.
3.  **Migrations**: If you change any models, run:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4.  **Frontend**: If you modify styles or templates using Tailwind, keep `npm run dev` running or run `npm run build`.
5.  **Testing**: Run tests frequently to avoid regressions.

## 📦 Dependency Management

-   **Python**: Dependencies are listed in `requirements.txt`.
-   **JavaScript**: Managed via `package.json` and `npm`.

## 🤖 Adding New AI Providers

To add a new AI provider (e.g., Anthropic):

1.  **Define Interface**: If the provider offers a new capability, add an ABC in `ai_engine/domain/interfaces.py`.
2.  **Create Adapter**: Implement the concrete class in `ai_engine/infrastructure/adapters/anthropic_adapter.py`.
3.  **Update Factory**: Modify `ai_engine/application/factory.py` to allow instantiating the new provider.

## 🧹 Code Quality

-   Follow PEP 8 for Python code.
-   Add Google-style docstrings to all new classes and functions.
-   Ensure 100% of new business logic is covered by unit tests.

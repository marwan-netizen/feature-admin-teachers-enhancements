# LingoPulse AI

LingoPulse AI is a world-class English proficiency assessment platform powered by advanced AI integrations (Groq, Gemini, OpenRouter) and structured for high scalability and maintainability.

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Node.js & npm (for frontend assets)
- Ollama (optional, for local AI features)

### Installation

1. **Clone and Setup Environment:**
   ```bash
   pip install -r requirements.txt
   # Configure your API keys in .env
   ```

2. **Database & Migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Running the Server:**
   ```bash
   python manage.py runserver
   ```

## 🧪 Testing

We use `pytest` for unit and integration tests.

```bash
python -m pytest
```

## 🛠 Architecture

This project follows a **Modular Monolith** architecture with **Clean Architecture** principles. For a deep dive into the design decisions, see [ARCHITECTURE.md](ARCHITECTURE.md).

## 🏗 Modular Structure

- **`accounts/`**: Unified user model, Student/Teacher/Admin profiles, and session-based auth.
- **`testing/`**: MCQ and AI-graded test engine (Reading, Listening, Writing, Speaking).
- **`classroom/`**: Virtual classrooms, assignments, and Jitsi-powered live sessions.
- **`ai_engine/`**: Integration layer for Ollama, Groq, Gemini, and OpenRouter (Port/Adapter pattern).
- **`core/`**: Common middleware, shared templates, and global static assets.

## 🛡 Production Readiness

- **Structured Logging:** JSON logs for production observability.
- **Global Error Handling:** Consistent error responses and traceback logging via custom middleware.
- **Health Monitoring:** `/health/` endpoint for load balancers and uptime checks.
- **Soft Delete:** Protected data management across all models.

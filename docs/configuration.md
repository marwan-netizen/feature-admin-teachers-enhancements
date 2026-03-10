# Configuration Reference

LingoPulse AI uses `django-environ` for environment-based configuration. All sensitive data and environment-specific settings should be stored in a `.env` file at the root of the project.

## 🔑 Required Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DEBUG` | Enable/Disable Django debug mode | `True` |
| `SECRET_KEY` | Django secret key for security | - |
| `APP_URL` | Base URL of the application | `http://localhost:8000` |
| `APP_KEY` | Application key for internal encryption/tests | - |

## 🤖 AI Provider Keys

| Variable | Description |
| :--- | :--- |
| `GROQ_API_KEY` | API Key for Groq Cloud (Test Generation) |
| `GEMINI_API_KEY` | API Key for Google Gemini (Evaluation) |
| `OPENROUTER_API_KEY` | API Key for OpenRouter (Listening/TTS) |
| `OLLAMA_URL` | URL for local Ollama instance (`http://localhost:11434`) |
| `OLLAMA_MODEL` | Model name for Ollama explanations (`tinyllama:1.1b`) |

## 📦 Database Configuration

By default, the application uses SQLite. To use a different database, configure `DATABASE_URL`:

```env
DATABASE_URL=postgres://user:password@localhost:5432/lingopulse
```

## 📧 Mail Configuration (Optional)

Used for notifications and account recovery.

| Variable | Description |
| :--- | :--- |
| `MAIL_HOST` | SMTP server host |
| `MAIL_PORT` | SMTP server port |
| `MAIL_USERNAME` | SMTP username |
| `MAIL_PASSWORD` | SMTP password |
| `MAIL_FROM_ADDRESS` | Sender email address |

## 📁 Storage Configuration

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MEDIA_ROOT` | Path to media files storage | `media/` |
| `MEDIA_URL` | URL prefix for media files | `/media/` |

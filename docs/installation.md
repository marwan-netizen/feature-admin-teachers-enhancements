# Installation Guide

This document provides detailed instructions for installing LingoPulse AI in various environments.

## 💻 Local Development Installation

### 1. System Requirements
- OS: Linux, macOS, or Windows (via WSL2 recommended).
- RAM: 8GB minimum (16GB recommended if running Ollama locally).

### 2. Python Environment
We recommend using `pyenv` to manage Python versions.
```bash
pyenv install 3.12.0
pyenv local 3.12.0
```

### 3. Database Setup
By default, the project uses SQLite for ease of development. If you wish to use PostgreSQL:
1.  Install PostgreSQL.
2.  Create a database: `CREATE DATABASE lingopulse;`.
3.  Update your `.env` file with database credentials.

### 4. Frontend Tooling
LingoPulse uses Vite for managing static assets and Tailwind CSS for styling.
```bash
npm install
# For development with HMR
npm run dev
# For production build
npm run build
```

## 🐋 Docker Installation

The project includes a `Dockerfile` and `docker-compose.yml` for simplified deployment.

### Development with Docker
```bash
docker-compose up
```
The `app` service is configured to use `network: host` in development to easily access Ollama running on the host machine.

### Production Docker Image
```bash
docker build -t lingopulse-ai:latest .
```

## 🤖 AI Provider Setup

LingoPulse AI requires API keys from several providers to function fully:

1.  **Groq**: Sign up at [groq.com](https://groq.com) and get an API key for fast Llama 3.1 inference.
2.  **Google Gemini**: Get an API key from [Google AI Studio](https://aistudio.google.com/) for test evaluation.
3.  **OpenRouter**: Sign up at [openrouter.ai](https://openrouter.ai) for access to Llama 3.3 and other models.
4.  **Ollama**: Install locally from [ollama.com](https://ollama.com) and pull the required model:
    ```bash
    ollama pull tinyllama:1.1b
    ```

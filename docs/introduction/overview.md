# Project Overview: LingoPulse AI

LingoPulse AI is an enterprise-grade English proficiency assessment platform migrated from a legacy Laravel codebase to a modern, modular Django architecture. It leverages advanced Artificial Intelligence to provide dynamic, personalized, and high-accuracy language evaluations.

## 🌟 Key Features

- **AI-Powered Test Generation**: Automatically generates Reading, Listening, Writing, and Speaking tests using Groq (Llama 3.1) and OpenRouter (Llama 3.3).
- **Dynamic Evaluation**: Real-time scoring and feedback for Writing and Speaking tests powered by Google Gemini 1.5.
- **Local AI Explanations**: Uses Ollama (local LLM) to provide instant streaming explanations for test results.
- **Comprehensive Testing Suite**: Covers all four major language skills with a mix of MCQ and open-ended assessments.
- **Virtual Classrooms**: Integrated classroom management for teachers, including assignments, grading, and live sessions.
- **Jitsi Integration**: Seamless real-time video sessions for online classes.
- **Modular Monolith Architecture**: Built with Clean Architecture principles to ensure scalability, testability, and maintainability.

## 🎯 Target Audience

- **Students**: Language learners looking for accurate, AI-driven proficiency assessments.
- **Teachers**: Educators who need a robust platform to manage classes, assignments, and track student progress.
- **Administrators**: System managers overseeing the entire platform and user base.

## 🛠 Tech Stack

- **Backend**: Django (Python 3.12+)
- **Frontend**: Vite, Tailwind CSS (Modern Asset Pipeline)
- **AI Integrations**: Groq, Google Gemini, OpenRouter, Ollama
- **Database**: SQLite (Development), PostgreSQL (Recommended for Production)
- **Containerization**: Docker & Docker Compose
- **Testing**: Pytest (Unit & Integration), Selenium (End-to-End)

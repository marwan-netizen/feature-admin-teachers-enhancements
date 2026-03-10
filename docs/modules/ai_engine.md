# AI Engine Module

The `ai_engine` module is the intelligence hub of LingoPulse AI. It abstracts various AI services behind a unified interface, allowing for easy provider switching and high testability.

## 🔌 Interfaces (Ports)

-   **`TextGenerationProvider`**: Interface for generating text (e.g., test passages, questions).
-   **`EvaluationProvider`**: Interface for grading writing and speaking responses.
-   **`TTSProvider`**: Interface for converting text to audio (Listening tests).
-   **`StreamingProvider`**: Interface for real-time token streaming (Explanations).

## 🚀 Adapters

-   **`GroqProvider`**: High-performance text generation using Llama 3.1.
-   **`GeminiProvider`**: Multimodal evaluation using Google Gemini 1.5.
-   **`OpenRouterProvider`**: Gateway for various models and TTS services.
-   **`Ollama` (Internal)**: Local LLM integration for cost-effective explanations.

## 🛠 Application Services

-   **`AIService`**: The main service used by other modules. It coordinates multiple providers to generate comprehensive tests or evaluate complex student responses.
-   **`AIServiceFactory`**: Responsible for instantiating the `AIService` with the correct concrete adapters based on configuration.

## 💬 Chat System

The module includes a built-in AI chatbot for students to practice English in a conversational setting, with message persistence and history tracking.

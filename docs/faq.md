# Frequently Asked Questions (FAQ)

### 1. Can I use LingoPulse AI without internet access?
Most core features (Test Generation, Evaluation) require internet access to communicate with cloud AI providers (Groq, Gemini). However, the platform supports local AI explanations via Ollama if it's installed and configured on your local machine.

### 2. Is my data shared with AI providers?
Only the minimal text data required for assessment (like your essay response or speaking transcription) is sent to providers. No personally identifiable information (PII) like your name or email is shared with Groq, Google, or OpenRouter.

### 3. What English levels are supported?
Currently, the platform is optimized for **Beginner** to **Intermediate** levels. The AI test generation prompts are tuned to create content appropriate for these levels.

### 4. How accurate is the AI grading?
The grading system uses Google Gemini 1.5, which is highly capable of language evaluation. For Speaking, we use transcription-based accuracy checks. While very accurate, we recommend teacher review for high-stakes assessments.

### 5. Can I add my own static tests?
Yes. Teachers can create tests manually through the Django admin panel or the database, which will be used as a fallback if dynamic AI generation is disabled or fails.

### 6. How do I join a live session?
Once a teacher creates an online session, a "Join Session" button will appear on your Student Dashboard. Clicking it will open a Jitsi Meet interface in your browser.

# API Endpoints Reference

## 🧠 AI Engine Endpoints

### 1. Ollama Explanation (Streaming)
Generates a real-time explanation for a test question using a local Ollama instance.

- **URL**: `/api/ollama/explain/`
- **Method**: `POST`
- **Auth**: None (Internal)
- **Request Body**:
  ```json
  {
    "question": "What is the capital of France?",
    "student_answer": "Berlin",
    "correct_answer": "Paris"
  }
  ```
- **Response**: `text/event-stream` returning chunks of tokens.

### 2. Chatbot History
Retrieves the message history for the current user's chatbot session.

- **URL**: `/chatbot/history/`
- **Method**: `GET`
- **Auth**: Required (Student)
- **Response**:
  ```json
  [
    {"role": "user", "content": "Hello!"},
    {"role": "model", "content": "How can I help you today?"}
  ]
  ```

### 3. Chatbot Send Message
Sends a message to the AI tutor and receives a response.

- **URL**: `/chatbot/send/`
- **Method**: `POST`
- **Auth**: Required (Student)
- **Request Parameters**: `message` (string)
- **Response**:
  ```json
  {
    "status": "success",
    "response": "Feedback from AI..."
  }
  ```

## 🏥 Health Endpoints

### 1. System Health Check
Returns the current status of the application and its dependencies.

- **URL**: `/health/`
- **Method**: `GET`
- **Auth**: None
- **Response**:
  ```json
  {
    "status": "healthy",
    "checks": {
      "database": "ok"
    }
  }
  ```

## 🏫 Classroom Endpoints

Note: Most classroom operations are currently handled via standard Django form submissions and redirects, but they expose the following logic:

- **Create Online Session**: `/teacher/session/create/` (`POST`)
- **Create Assignment**: `/teacher/assignment/create/` (`POST`)
- **Submit Assignment**: `/assignment/submit/<id>/` (`POST`)
- **Grade Submission**: `/submission/grade/<id>/` (`POST`)

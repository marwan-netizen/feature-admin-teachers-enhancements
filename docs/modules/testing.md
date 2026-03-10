# Testing Module

The `testing` module manages the core proficiency assessment logic of the platform.

## 📝 Test Types

1.  **Reading**: Multiple-choice questions based on AI-generated or static passages.
2.  **Listening**: MCQs based on AI-generated audio or pre-recorded clips.
3.  **Writing**: Open-ended essay responses evaluated by AI.
4.  **Speaking**: Reading aloud passages, transcribed and evaluated for accuracy by AI.

## 🔄 Dynamic Test Flow

1.  **Initiation**: User starts a test session.
2.  **Generation**: `TestingService` calls `AIService` to generate a unique set of tests for all four skills.
3.  **Persistence**: Generated tests, questions, and options are saved to the database.
4.  **Execution**: User proceeds through the skills in sequence.
5.  **Grading**:
    - MCQs are graded instantly against stored correct answers.
    - Writing/Speaking responses are sent to the AI Engine for evaluation.
6.  **Results**: A consolidated `Result` record is created, and the student can view their scores and feedback.

## 🏗 Persistence Layer

-   **`Test`**: Represents a single assessment (e.g., "Beginner Reading Test").
-   **`Question` & `Option`**: The structure for MCQ-based assessments.
-   **`StudentAnswer`**: Stores the raw response from the student.
-   **`Evaluation`**: Stores the AI-generated score and feedback for open-ended questions.

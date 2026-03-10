# Classroom Module

The `classroom` module provides the environment for structured learning and teacher-student interaction.

## 🏫 Key Features

-   **Class Management**: Teachers can create classes and enroll students.
-   **Assignments**: Support for creating assignments with file attachments and deadlines.
-   **Submission & Versioning**: Students can submit multiple versions of an assignment.
-   **Grading System**: Teachers can grade assignments and provide qualitative feedback.
-   **Online Sessions**: Integration with Jitsi Meet for scheduled live video classes.

## 🏗 Data Structure

-   **`Classes`**: The central entity representing a course or class.
-   **`Assignment`**: Linked to a class and teacher.
-   **`AssignmentSubmission`**: Tracks a student's response to an assignment.
-   **`OnlineSession`**: Stores Jitsi room details and session schedules.
-   **`Grade`**: Consolidated grading records for various assessments (midterm, final, etc.).

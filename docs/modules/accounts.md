# Accounts Module

The `accounts` module manages user identities, authentication, and profile roles.

## 👥 User Roles

-   **Student**: Can take proficiency tests, view results, join classes, and submit assignments.
-   **Teacher**: Can create classes, manage assignments, grade submissions, and start online sessions.
-   **Admin**: Full system access, including user management and platform configuration.

## 🏗 Models

-   **`User`**: Custom user model using `email` as the primary identifier. Inherits from `AbstractBaseUser` and `SoftDeleteModel`.
-   **`Student`**: Extension of `User` containing student-specific data (e.g., current level).
-   **`Teacher`**: Extension of `User` for educator profiles.
-   **`Admin`**: Extension of `User` for administrative profiles.

## 🔐 Authentication Flow

The module implements a standard session-based authentication system.
- **Registration**: Handles both standard signup and a simplified registration flow for students.
- **Login**: Authenticates users and redirects them to their respective dashboards based on role.
- **Authorization**: Role-based access control is enforced at the view level.

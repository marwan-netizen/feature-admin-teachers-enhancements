# Core Module

The `core` module provides shared functionality, base classes, and global configurations for the LingoPulse AI platform.

## 🛠 Base Components

-   **`SoftDeleteModel`**: An abstract base model that implements soft deletion. Instead of removing records from the database, it sets a `deleted_at` timestamp.
-   **`ActivityLog`**: A global logging mechanism to track user actions (CRUD operations) for audit purposes.
-   **`Notification`**: A system for managing internal platform notifications.

## 🛡 Middleware

-   **`ExceptionHandlerMiddleware`**: Intercepts unhandled exceptions and returns structured JSON errors in production, while providing detailed tracebacks in development.

## 🏥 Health Monitoring

-   **`/health/`**: A public endpoint that performs basic checks (e.g., database connectivity) to ensure system uptime.

## 🎨 Shared Assets

-   Base HTML templates, global CSS (Tailwind), and shared static images are managed within this module.

# API Authentication

LingoPulse AI uses standard Django session authentication for most of its internal API endpoints.

## 🍪 Session Authentication

For requests made from the browser, the application uses cookies to manage authentication.

1.  **Login**: Send a `POST` request to `/auth/login/` with `email` and `password`.
2.  **Session Cookie**: Upon successful login, the server sets a `sessionid` cookie.
3.  **Subsequent Requests**: Include this cookie in all subsequent requests.

## 🛡 CSRF Protection

All state-changing requests (`POST`, `PUT`, `DELETE`, `PATCH`) must include a CSRF token.

- **Header**: `X-CSRFToken`
- **Cookie**: `csrftoken`

In your JavaScript/AJAX calls, ensure you extract the CSRF token from the cookie and send it in the header.

## 🔐 Role-Based Access

Endpoints are protected by role-based decorators. If a user tries to access an endpoint they don't have permission for (e.g., a student trying to access teacher dashboards), a `403 Forbidden` or a redirect to the login page will be issued.

# API Overview

LingoPulse AI provides a set of internal and external APIs to facilitate test generation, evaluation, and student interaction.

## 📡 Protocol
All APIs communicate over **HTTPS** using standard **RESTful** principles. Responses are returned in **JSON** format.

## 🌐 Base URL
The base URL for all API requests depends on your environment:
- **Local**: `http://localhost:8000`
- **Production**: `https://api.lingopulse.ai` (example)

## ⚠️ Content Type
All `POST`, `PUT`, and `PATCH` requests must include the `Content-Type: application/json` header.

## 🚦 Status Codes

| Code | Description |
| :--- | :--- |
| `200 OK` | Request successful. |
| `201 Created` | Resource created successfully. |
| `400 Bad Request` | Invalid parameters or payload. |
| `401 Unauthorized` | Authentication required or failed. |
| `403 Forbidden` | Insufficient permissions for the resource. |
| `404 Not Found` | Resource not found. |
| `405 Method Not Allowed` | Incorrect HTTP method used. |
| `500 Internal Server Error` | An unexpected error occurred on the server. |

## 🛡 Security
Most endpoints require an active session or a valid CSRF token for state-changing operations. See [Authentication](authentication.md) for details.

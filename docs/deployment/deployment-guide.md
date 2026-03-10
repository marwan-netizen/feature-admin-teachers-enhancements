# Deployment Guide

This document outlines the steps for deploying LingoPulse AI to a production environment.

## 🏭 Production Requirements

- **Server**: Linux (Ubuntu 22.04 LTS recommended).
- **Python**: 3.12+.
- **Database**: PostgreSQL 15+.
- **Web Server**: Nginx.
- **Application Server**: Gunicorn or Uvicorn (for ASGI).
- **Process Manager**: Systemd or Supervisor.

## 🚀 Manual Deployment Steps

1.  **Clone & Install**:
    ```bash
    git clone https://github.com/your-org/lingopulse-ai.git /var/www/lingopulse
    cd /var/www/lingopulse
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Environment Configuration**:
    Configure a production `.env` file. Set `DEBUG=False` and generate a strong `SECRET_KEY`.

3.  **Static & Media Files**:
    ```bash
    python manage.py collectstatic
    mkdir -p media
    ```

4.  **Database**:
    ```bash
    python manage.py migrate
    ```

5.  **Gunicorn Setup**:
    Create a systemd service for Gunicorn.
    ```ini
    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=www-data
    Group=www-data
    WorkingDirectory=/var/www/lingopulse
    ExecStart=/var/www/lingopulse/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock lingopulse.wsgi:application
    ```

6.  **Nginx Setup**:
    Configure Nginx to proxy requests to Gunicorn and serve static/media files directly.

## 🐳 Docker Deployment (Recommended)

For production, use the provided `Dockerfile`.

```bash
docker build -t lingopulse-prod .
docker run -d --name lingopulse-app -p 80:80 --env-file .env lingopulse-prod
```

## 📈 Scaling

- **Horizontal**: The stateless nature of the application allows for running multiple containers behind a load balancer.
- **Database**: Use a managed RDS instance (e.g., AWS RDS, GCP Cloud SQL) for high availability.
- **Media**: For multi-server setups, use S3-compatible storage (e.g., AWS S3, DigitalOcean Spaces) for media files.

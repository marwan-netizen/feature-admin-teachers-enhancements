# Stage 1: Build frontend assets
FROM node:20-slim AS frontend-builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Python environment
FROM python:3.12-slim
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y     build-essential     libpq-dev     curl     --no-install-recommends     && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN groupadd -g 1000 appuser &&     useradd -r -u 1000 -g appuser appuser

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=appuser:appuser . .

# Copy built assets from frontend-builder
COPY --from=frontend-builder --chown=appuser:appuser /app/core/static/dist ./core/static/dist

# Create necessary directories and set permissions
RUN mkdir -p /app/media /app/staticfiles &&     chown -R appuser:appuser /app/media /app/staticfiles

# Set up entrypoint
COPY --chown=appuser:appuser docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Switch to non-root user
USER appuser

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "lingopulse.asgi:application"]

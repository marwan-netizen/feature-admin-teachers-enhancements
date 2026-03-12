# Infrastructure Hardening Guide

## 1. Container Security
- **Non-Root Execution**: The application runs as `appuser` (UID 1000) instead of root.
- **No New Privileges**: Docker containers are configured with `no-new-privileges:true` to prevent privilege escalation.
- **Minimal Images**: Used `python:3.12-slim` and `alpine` variants to reduce attack surface.

## 2. Network Segmentation
- **Frontend Network**: Only the `web` service is exposed to the frontend network.
- **Backend Network**: Internal communication between web, db, and redis happens on an isolated internal network.
- **Database Isolation**: The database and redis are NOT accessible from outside the Docker host.

## 3. Secret Management
- **Environment Variables**: All secrets are passed via environment variables, not hardcoded.
- **No Commits**: `.env` file must never be committed to the repository.

## 4. Host Security (Recommendations)
- **Automatic Updates**: Enable unattended-upgrades on the host OS.
- **SSH Hardening**: Disable root login and password authentication; use SSH keys only.
- **Firewall**: Use `ufw` or `iptables` to allow only ports 80/443 (via a reverse proxy like Nginx).
- **TLS 1.3**: Configure the reverse proxy (Nginx/Traefik) to support TLS 1.3 only and secure ciphers.

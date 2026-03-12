# Disaster Recovery & Backup Plan

## 1. Backup Strategy
- **Database**: Automated daily snapshots of Postgres with 30-day retention.
- **Media/Files**: Replicated storage for user uploads.
- **Off-site**: Backups must be stored in a different physical region from the production server.

## 2. Recovery Time Objective (RTO)
- Target: Full system restoration within 4 hours.

## 3. Recovery Point Objective (RPO)
- Target: Maximum data loss of 24 hours (last daily backup).

## 4. Testing
- Recovery drills must be performed quarterly to ensure backup integrity and team readiness.

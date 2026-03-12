# Incident Response Plan (IRP)

## 1. Incident Categories
- **Level 1 (Critical)**: Data breach, full system outage, compromise of KMS Master Key.
- **Level 2 (High)**: Individual account takeover, persistent XSS found in production.
- **Level 3 (Medium)**: Denial of Service (DoS) attack, unauthorized access to non-sensitive data.

## 2. Response Steps (PICERL)
1. **Preparation**: Maintaining security tools, backups, and this IRP.
2. **Identification**: Detecting the incident via logs (ActivityLog) or monitoring alerts.
3. **Containment**: Isolating affected systems, rotating compromised keys.
4. **Eradication**: Removing the root cause (fixing vulnerability, deleting malware).
5. **Recovery**: Restoring systems from clean backups.
6. **Lessons Learned**: Post-incident review and updating security controls.

## 3. Communication Plan
- **Internal**: Notify Security Team and Management immediately.
- **External**: If PII is leaked, notify affected users and regulatory bodies within 72 hours (as per GDPR guidelines).

## 4. Key Rotation Procedure
In case of a suspected breach:
1. Revoke existing `APP_KEY` and `KMS_MASTER_KEY`.
2. Generate new keys using cryptographically secure methods.
3. Update environment variables in the production environment.
4. Force logout all users and require password reset if necessary.

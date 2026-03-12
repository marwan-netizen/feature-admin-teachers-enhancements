# Cryptography and Key Management Policy

## 1. Approved Algorithms
- **Symmetric Encryption**: AES-256-GCM (Authenticated Encryption).
- **Password Hashing**: Argon2id (Memory-hard, side-channel resistant).
- **Asymmetric Encryption**: Ed25519 for digital signatures.
- **Message Authentication**: HMAC-SHA256.

## 2. Key Management System (KMS)
- **Master Key**: Stored as a 32-byte base64 encoded string in `KMS_MASTER_KEY` environment variable.
- **Key Rotation**: Mandatory every 90 days.
- **Access Control**: Only the Application Server and authorized Security Admins can access KMS keys.

## 3. Data Protection
- **Personal Data (PII)**: Encrypted at the field level before being stored in the database.
- **Data in Transit**: TLS 1.3 only for all external and internal communication.
- **Backups**: All database backups must be encrypted using the Master Key.

## 4. Implementation Guidelines
- Never use `hashlib.sha1` or `hashlib.md5` for security-sensitive operations.
- Always use `secrets` module for generating random tokens or nonces.
- Use `KMSManager` for any cryptographic operations.

# Supply Chain Security Policy

## 1. Dependency Management
- **Pinning**: All dependencies in `requirements.txt` must be pinned to a specific version.
- **Auditing**: Monthly audit of all libraries using `safety` and `pip-audit`.
- **Minimalism**: Avoid adding new dependencies unless absolutely necessary.

## 2. CI/CD Security
- **Mandatory Scans**: No pull request can be merged without passing SAST, secret scanning, and dependency checks.
- **Signed Commits**: All developers must use GPG-signed commits.
- **Secrets in CI**: Use GitHub Actions Secrets; never echo secrets in logs.

## 3. SBOM (Software Bill of Materials)
- The system generates an SBOM on every build to track all components and their versions.
- SBOMs are stored in build artifacts for 90 days.

## 4. Vendor Risk Management
- Evaluate security practices of external AI API providers (Groq, Gemini, etc.) annually.
- Ensure data processing agreements (DPA) are in place where required by law.

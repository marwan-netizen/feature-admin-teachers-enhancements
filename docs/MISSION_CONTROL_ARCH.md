# LingoPulse Mission Control - Enterprise Architecture

## 1. Vision
LingoPulse Mission Control is a next-generation operational intelligence platform designed for high-scale English proficiency assessment. It transcends traditional administrative interfaces to provide a "Mission Control" experience for engineers, educators, and administrators.

## 2. Core Architecture Layers

### Layer 1: Interface (SaaS Dashboards)
- **Technology**: `django-unfold`, HTMX, Alpine.js.
- **Responsibility**: Provides a modular, high-performance UI for data management, system monitoring, and AI insights.
- **Components**:
    - **Global Dashboard**: Aggregates platform-wide metrics (Active Users, System Health, AI Insights).
    - **Module Dashboards**: Specialized views for Classroom, Testing, and Analytics modules.

### Layer 2: Operational Intelligence (AI Agents)
- **Technology**: `enterprise.ai.agents`.
- **Responsibility**: Proactive monitoring and optimization using specialized AI agents.
- **Agents**:
    - **OptimizationAgent**: Identifies performance bottlenecks and cache opportunities.
    - **SecurityAgent**: Detects anomalous login patterns and permission escalations.
    - **HealthAgent**: Monitors infrastructure stability and Celery worker efficiency.

### Layer 3: Service Layer (Operational Logic)
- **Technology**: `enterprise.services`.
- **Responsibility**: Decoupled business logic for complex cross-cutting operations.
- **Services**:
    - **SystemHealthService**: Aggregates metrics from `psutil` and Prometheus.
    - **DiagnosticService**: Orchestrates on-demand system health tests.
    - **AuditService**: Analyzes historical records for security auditing.

### Layer 4: Real-time Communication
- **Technology**: Django Channels (WebSockets), Redis.
- **Responsibility**: Pushing live system metrics, notifications, and log streams to the dashboard.

### Layer 5: Infrastructure & Monitoring
- **Technology**: `psutil`, `Prometheus`, `Sentry`, `Celery`.
- **Responsibility**: Raw data collection and error tracking for the entire platform.

## 3. Data Flow
1. **Infrastructure Layer** collects raw metrics (CPU, DB Load, Error rates).
2. **AI Agents** ingest these metrics and historical data to generate "Insights".
3. **Mission Control Dashboard** aggregates these Insights and Metrics.
4. **Channels** push updates to the UI for real-time visibility.
5. **Administrators** take "Quick Actions" via the UI, which trigger **Services**.

## 4. Security Model
- **RBAC**: Fine-grained permissions using `django-guardian`.
- **MFA**: Mandatory Two-Factor Authentication for all administrative access.
- **Audit**: Comprehensive change tracking via `django-simple-history` and centralized `ActivityLog`.

# Getting Started with LingoPulse AI

Follow this guide to get LingoPulse AI up and running on your local development environment.

## 📋 Prerequisites

Ensure you have the following installed:

- **Python 3.12+**
- **Node.js & npm** (for frontend assets)
- **Docker & Docker Compose** (optional, for containerized setup)
- **Ollama** (optional, for local AI explanation features)

## ⚡ Quick Start (Local Setup)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-org/lingopulse-ai.git
    cd lingopulse-ai
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory (refer to [Configuration](configuration.md)).

5.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Build Frontend Assets:**
    ```bash
    npm install
    npm run build
    ```

7.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

## 🐳 Running with Docker

1.  **Build and Start Containers:**
    ```bash
    docker-compose up --build
    ```

2.  **Access the Application:**
    Open `http://localhost:8000` in your browser.

## 🧪 Verifying the Setup

Run the test suite to ensure everything is working correctly:

```bash
APP_KEY=secret python -m pytest
```

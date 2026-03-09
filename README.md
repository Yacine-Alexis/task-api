# Task API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A production-ready RESTful API for task management built with modern Python best practices.**

[Features](#-features) •
[Architecture](#-architecture) •
[Quick Start](#-quick-start) •
[API Documentation](#-api-documentation) •
[Testing](#-testing)

</div>

---

## 📋 Overview

Task API is a full-featured backend service demonstrating enterprise-level software engineering practices. Built with FastAPI and PostgreSQL, it provides a robust foundation for task and project management with secure authentication, comprehensive validation, and extensive test coverage.

This project showcases:

- **Clean Architecture** — Separation of concerns with dedicated layers for API, services, and data access
- **Modern Async Python** — Fully asynchronous with SQLAlchemy 2.0 and asyncpg
- **Security First** — JWT-based authentication with bcrypt password hashing
- **Production Ready** — Docker containerization, CI/CD pipelines, and comprehensive logging

---

## ✨ Features

### Core Functionality

| Feature                      | Description                                                              |
| :--------------------------- | :----------------------------------------------------------------------- |
| **Task Management**    | Create, update, delete, and organize tasks with priorities and due dates |
| **Project Workspaces** | Group tasks into projects with color coding and archival support         |
| **Labels & Tags**      | Flexible labeling system for task categorization                         |
| **Smart Filtering**    | Filter tasks by status, priority, project, and date ranges               |
| **Pagination**         | Efficient cursor-based pagination for large datasets                     |

### Authentication & Security

| Feature                      | Description                                            |
| :--------------------------- | :----------------------------------------------------- |
| **JWT Authentication** | Secure token-based auth with access and refresh tokens |
| **Password Security**  | bcrypt hashing with configurable work factors          |
| **Role-Based Access**  | Users can only access their own resources              |
| **Input Validation**   | Comprehensive request validation with Pydantic v2      |

### Developer Experience

| Feature                   | Description                                       |
| :------------------------ | :------------------------------------------------ |
| **OpenAPI/Swagger** | Interactive API documentation at `/api/v1/docs` |
| **Type Safety**     | Full type hints throughout the codebase           |
| **Async Support**   | Non-blocking I/O for high concurrency             |
| **Hot Reload**      | Development server with automatic reloading       |

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        API Layer (FastAPI)                       │
│   ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌─────────────────┐  │
│   │  Auth   │  │  Tasks  │  │ Projects │  │     Labels      │  │
│   └────┬────┘  └────┬────┘  └────┬─────┘  └────────┬────────┘  │
└────────┼────────────┼────────────┼─────────────────┼────────────┘
         │            │            │                 │
┌────────┴────────────┴────────────┴─────────────────┴────────────┐
│                       Service Layer                              │
│         Business Logic • Validation • Authorization              │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────┴────────────────────────────────┐
│                      Repository Layer                            │
│              Data Access • Query Building • Caching              │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────┴────────────────────────────────┐
│                     Database (PostgreSQL)                        │
│           Users • Tasks • Projects • Labels • Logs               │
└─────────────────────────────────────────────────────────────────┘
```

### Project Structure

```
task-api/
├── app/
│   ├── api/v1/              # API routes and endpoints
│   │   └── endpoints/       # Resource-specific handlers
│   ├── core/                # Configuration, security, database
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic validation schemas
│   ├── services/            # Business logic layer
│   ├── repositories/        # Data access layer
│   └── utils/               # Helpers and exceptions
├── alembic/                 # Database migrations
├── tests/                   # Unit and integration tests
├── docker-compose.yml       # Container orchestration
└── Dockerfile               # Application container
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+ (or Docker)
- pip or Poetry

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Yacine-Alexis/task-api.git
   cd task-api
   ```
2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment**

   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and secret key
   ```
5. **Run database migrations**

   ```bash
   alembic upgrade head
   ```
6. **Start the development server**

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Using Docker

```bash
# Start all services (API + PostgreSQL)
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

---

## 📖 API Documentation

Once running, access the interactive documentation:

- **Swagger UI**: http://localhost:8000/api/v1/docs
- **ReDoc**: http://localhost:8000/api/v1/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

### Endpoints Overview

| Method     | Endpoint                  | Description                 |
| :--------- | :------------------------ | :-------------------------- |
| `POST`   | `/api/v1/auth/register` | Register a new user         |
| `POST`   | `/api/v1/auth/login`    | Authenticate and get tokens |
| `POST`   | `/api/v1/auth/refresh`  | Refresh access token        |
| `GET`    | `/api/v1/users/me`      | Get current user profile    |
| `PATCH`  | `/api/v1/users/me`      | Update user profile         |
| `GET`    | `/api/v1/tasks`         | List tasks (with filters)   |
| `POST`   | `/api/v1/tasks`         | Create a new task           |
| `GET`    | `/api/v1/tasks/{id}`    | Get task details            |
| `PATCH`  | `/api/v1/tasks/{id}`    | Update a task               |
| `DELETE` | `/api/v1/tasks/{id}`    | Delete a task               |
| `GET`    | `/api/v1/projects`      | List projects               |
| `POST`   | `/api/v1/projects`      | Create a project            |
| `GET`    | `/api/v1/labels`        | List labels                 |
| `POST`   | `/api/v1/labels`        | Create a label              |

### Example Request

```bash
# Register a new user
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!",
    "full_name": "John Doe"
  }'

# Create a task (authenticated)
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive API docs",
    "priority": "high",
    "due_date": "2026-03-15T18:00:00Z"
  }'
```

---

## 🧪 Testing

The project includes comprehensive unit and integration tests.

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_security.py -v

# Run only integration tests
pytest tests/integration/ -v
```

### Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── unit/                    # Unit tests (no database)
│   └── test_security.py     # Security module tests
└── integration/             # Integration tests (with database)
    └── test_tasks.py        # Task endpoint tests
```

---

## ⚙️ Configuration

Environment variables (`.env`):

| Variable                        | Description                  | Default    |
| :------------------------------ | :--------------------------- | :--------- |
| `PROJECT_NAME`                | API title in docs            | Task API   |
| `SECRET_KEY`                  | JWT signing key              | (required) |
| `DATABASE_URL`                | PostgreSQL connection string | (required) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT access token TTL         | 30         |
| `REFRESH_TOKEN_EXPIRE_DAYS`   | JWT refresh token TTL        | 7          |

---

## 🛠 Tech Stack

| Technology                 | Purpose                                           |
| :------------------------- | :------------------------------------------------ |
| **FastAPI**          | Modern async web framework with automatic OpenAPI |
| **SQLAlchemy 2.0**   | Async ORM with type-safe queries                  |
| **PostgreSQL**       | Production-grade relational database              |
| **Pydantic v2**      | Data validation and serialization                 |
| **Alembic**          | Database schema migrations                        |
| **python-jose**      | JWT token encoding/decoding                       |
| **passlib + bcrypt** | Secure password hashing                           |
| **pytest**           | Testing framework with async support              |
| **Docker**           | Containerization and deployment                   |
| **GitHub Actions**   | CI/CD pipeline automation                         |

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built for learning and portfolio demonstration**

</div>

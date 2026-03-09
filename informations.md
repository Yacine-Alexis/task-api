# Task-API: Project Information

## 📋 What is Task-API?

Task-API is a **modern, production-ready RESTful API** for task and project management. It serves as a backend service that enables developers to integrate task management capabilities into their applications, similar to how Todoist, Asana, or Trello expose their APIs.

This project demonstrates proficiency in:
- Backend API development
- Database design and ORM usage
- Authentication & Authorization
- Clean Architecture principles
- API documentation (OpenAPI/Swagger)
- Testing strategies
- Containerization with Docker

---

## 🎯 What Tasks Should It Perform?

### Core Features

| Feature | Description |
|---------|-------------|
| **User Management** | Registration, login, JWT authentication, profile management |
| **Task CRUD** | Create, read, update, delete tasks with full validation |
| **Project Organization** | Group tasks into projects/workspaces |
| **Labels & Tags** | Categorize tasks with custom labels |
| **Priority Levels** | Urgent, High, Medium, Low priority support |
| **Due Dates** | Set deadlines with timezone support |
| **Status Tracking** | Todo → In Progress → Completed workflow |
| **Search & Filter** | Full-text search, filter by date/status/priority |
| **Collaboration** | Assign tasks to team members |
| **Activity Logs** | Track changes and task history |

### API Endpoints Overview

```
Authentication:
POST   /api/v1/auth/register     - Register new user
POST   /api/v1/auth/login        - Login and get JWT
POST   /api/v1/auth/refresh      - Refresh access token
POST   /api/v1/auth/logout       - Invalidate token

Users:
GET    /api/v1/users/me          - Get current user profile
PATCH  /api/v1/users/me          - Update profile
DELETE /api/v1/users/me          - Delete account

Projects:
GET    /api/v1/projects          - List all projects
POST   /api/v1/projects          - Create project
GET    /api/v1/projects/{id}     - Get project details
PATCH  /api/v1/projects/{id}     - Update project
DELETE /api/v1/projects/{id}     - Delete project

Tasks:
GET    /api/v1/tasks             - List tasks (with filters)
POST   /api/v1/tasks             - Create task
GET    /api/v1/tasks/{id}        - Get task details
PATCH  /api/v1/tasks/{id}        - Update task
DELETE /api/v1/tasks/{id}        - Delete task
POST   /api/v1/tasks/{id}/assign - Assign task to user
PATCH  /api/v1/tasks/{id}/status - Update task status

Labels:
GET    /api/v1/labels            - List labels
POST   /api/v1/labels            - Create label
DELETE /api/v1/labels/{id}       - Delete label
```

---

## 💼 Market Utility & Relevance (2026)

### Why This Project Matters

1. **High Demand for API Developers**
   - Companies are API-first; backend developers who can design clean, documented APIs are in high demand
   - Task management is a domain every recruiter understands instantly

2. **Demonstrates Real-World Skills**
   - Authentication (JWT) - security is critical
   - Database design (relations, indexes) - data modeling skills
   - Error handling & validation - production-ready code
   - Testing - shows professional development practices

3. **Extensible Architecture**
   - Can be extended with: notifications, webhooks, real-time updates (WebSockets)
   - Shows understanding of scalable system design

4. **Industry-Relevant Tech Stack**
   - FastAPI is growing rapidly in enterprise environments
   - PostgreSQL remains the most wanted database
   - Docker/containerization is standard

### Competitive Edge

| What Employers See | What It Demonstrates |
|--------------------|----------------------|
| Clean folder structure | Organized thinking, maintainability |
| Comprehensive tests | Quality-focused development |
| API documentation | Communication & user empathy |
| Docker support | DevOps awareness |
| Type hints & validation | Modern Python practices |

---

## 🛠️ Development & Implementation

### Tech Stack

| Layer | Technology |
|-------|------------|
| **Framework** | FastAPI (Python 3.11+) |
| **Database** | PostgreSQL 15 |
| **ORM** | SQLAlchemy 2.0 |
| **Migrations** | Alembic |
| **Authentication** | JWT (python-jose) + bcrypt |
| **Validation** | Pydantic v2 |
| **Testing** | pytest + httpx |
| **Documentation** | OpenAPI (auto-generated) |
| **Containerization** | Docker + Docker Compose |
| **CI/CD** | GitHub Actions |

### Development Phases

#### Phase 1: Foundation (Week 1)
- [ ] Project setup with Poetry/pip
- [ ] Database models (User, Task, Project, Label)
- [ ] Alembic migrations
- [ ] Basic CRUD operations
- [ ] Input validation with Pydantic

#### Phase 2: Authentication (Week 2)
- [ ] User registration with email validation
- [ ] Password hashing with bcrypt
- [ ] JWT token generation and refresh
- [ ] Protected route middleware
- [ ] Role-based access (optional)

#### Phase 3: Core Features (Week 3)
- [ ] Task filtering and search
- [ ] Project-task relationships
- [ ] Labels/tags system
- [ ] Task assignment
- [ ] Activity logging

#### Phase 4: Polish (Week 4)
- [ ] Comprehensive error handling
- [ ] Rate limiting
- [ ] Unit and integration tests (80%+ coverage)
- [ ] API documentation
- [ ] Docker setup
- [ ] GitHub Actions CI/CD

### Database Schema

```sql
-- Core tables
users (id, email, hashed_password, full_name, is_active, created_at)
projects (id, name, description, owner_id, created_at, updated_at)
tasks (id, title, description, status, priority, due_date, project_id, assignee_id, creator_id, created_at, updated_at)
labels (id, name, color, user_id)
task_labels (task_id, label_id)  -- Many-to-many
activity_logs (id, task_id, user_id, action, details, created_at)
```

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/taskapi

# Security
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# App
DEBUG=false
API_V1_PREFIX=/api/v1
PROJECT_NAME=Task-API
```

---

## 🚀 Getting Started (After Implementation)

```bash
# Clone the repository
git clone https://github.com/Yacine-Alexis/task-api.git
cd task-api

# Setup with Docker (recommended)
docker-compose up -d

# Or local setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload

# Run tests
pytest -v --cov=app

# Access API docs
open http://localhost:8000/docs
```

---

## 📚 Resources for Implementation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Alembic Migrations](https://alembic.sqlalchemy.org/)
- [Pydantic v2 Docs](https://docs.pydantic.dev/latest/)
- [JWT Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)

---

## ✅ Portfolio Impact Checklist

- [ ] Clear README with badges and demo GIF
- [ ] Live API demo (Render/Railway/Fly.io)
- [ ] Postman collection for easy testing
- [ ] 80%+ test coverage badge
- [ ] Clean commit history (conventional commits)
- [ ] Issue templates and PR templates
- [ ] Contributing guidelines

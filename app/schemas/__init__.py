"""
Pydantic Schemas Package

Contains Pydantic models for request/response validation and serialization.

Schema Naming Convention:
- {Model}Create: For creating new records (POST requests)
- {Model}Update: For partial updates (PATCH requests)
- {Model}Response: For API responses (includes id, timestamps)
- {Model}InDB: Internal use, includes hashed_password etc.

Each schema module corresponds to a model:
- user.py: UserCreate, UserUpdate, UserResponse, Token, TokenPayload
- task.py: TaskCreate, TaskUpdate, TaskResponse, TaskList
- project.py: ProjectCreate, ProjectUpdate, ProjectResponse
- label.py: LabelCreate, LabelResponse

Pydantic v2 Features Used:
- model_validator for cross-field validation
- field_validator for single-field validation
- ConfigDict with from_attributes=True for ORM mode
"""

# Re-export commonly used schemas
# from app.schemas.user import UserCreate, UserResponse, Token
# from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
# from app.schemas.project import ProjectCreate, ProjectResponse
# from app.schemas.label import LabelCreate, LabelResponse

"""
Task Schemas

Pydantic models for task operations.

Schemas:
- TaskCreate: New task payload
- TaskUpdate: Partial task update
- TaskResponse: Full task with relationships
- TaskList: Paginated list of tasks
- TaskFilter: Query parameters for filtering

Enum Schemas:
- TaskStatusEnum: todo, in_progress, completed
- TaskPriorityEnum: low, medium, high, urgent

Response Features:
- Includes nested creator/assignee info (UserResponse)
- Includes project summary
- Includes attached labels
"""

from datetime import datetime
from uuid import UUID
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class TaskStatusEnum(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TaskPriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatusEnum = TaskStatusEnum.TODO
    priority: TaskPriorityEnum = TaskPriorityEnum.MEDIUM
    due_date: datetime | None = None
    project_id: UUID | None = None
    assignee_id: UUID | None = None
    label_ids: list[UUID] = []


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatusEnum | None = None
    priority: TaskPriorityEnum | None = None
    due_date: datetime | None = None
    project_id: UUID | None = None
    assignee_id: UUID | None = None
    label_ids: list[UUID] | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: TaskStatusEnum
    priority: TaskPriorityEnum
    due_date: datetime | None
    project_id: UUID | None
    creator_id: UUID
    assignee_id: UUID | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TaskList(BaseModel):
    items: list[TaskResponse]
    total: int
    page: int
    per_page: int
    pages: int

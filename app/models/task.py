"""
Task Model

Represents an individual task item.

Table: tasks

Columns:
- id (UUID): Primary key
- title (String): Task title (required, max 255 chars)
- description (Text): Detailed task description (optional)
- status (Enum): Current status (todo, in_progress, completed)
- priority (Enum): Priority level (low, medium, high, urgent)
- due_date (DateTime): Task deadline (optional)
- project_id (UUID): Foreign key to projects table
- creator_id (UUID): Foreign key to users (who created)
- assignee_id (UUID): Foreign key to users (who's assigned)
- created_at (DateTime): Creation timestamp
- updated_at (DateTime): Last update timestamp

Relationships:
- project: Parent project
- creator: User who created the task
- assignee: User assigned to complete the task
- labels: Many-to-many with labels via task_labels
- activity_logs: History of changes

Indexes:
- ix_tasks_status: Filter by status
- ix_tasks_due_date: Sort/filter by deadline
- ix_tasks_project_id: Tasks within a project
"""

# TODO: Implementation
# import enum
# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from app.core.database import Base
#
# class TaskStatus(str, enum.Enum):
#     TODO = "todo"
#     IN_PROGRESS = "in_progress"
#     COMPLETED = "completed"
#
# class TaskPriority(str, enum.Enum):
#     LOW = "low"
#     MEDIUM = "medium"
#     HIGH = "high"
#     URGENT = "urgent"
#
# class Task(Base):
#     __tablename__ = "tasks"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     title = Column(String(255), nullable=False)
#     description = Column(Text)
#     status = Column(Enum(TaskStatus), default=TaskStatus.TODO, index=True)
#     priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)
#     due_date = Column(DateTime, index=True)
#     project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), index=True)
#     creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#     # Relationships
#     project = relationship("Project", back_populates="tasks")
#     creator = relationship("User", back_populates="tasks_created", foreign_keys=[creator_id])
#     assignee = relationship("User", back_populates="tasks_assigned", foreign_keys=[assignee_id])
#     labels = relationship("Label", secondary="task_labels", back_populates="tasks")

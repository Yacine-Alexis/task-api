"""
User Model

Represents a user account in the system.

Table: users

Columns:
- id (UUID): Primary key, auto-generated
- email (String): Unique, indexed, user's email address
- hashed_password (String): Bcrypt-hashed password
- full_name (String): User's display name
- is_active (Boolean): Account status (for soft disable)
- is_superuser (Boolean): Admin privileges flag
- created_at (DateTime): Account creation timestamp
- updated_at (DateTime): Last modification timestamp

Relationships:
- tasks_created: Tasks created by this user
- tasks_assigned: Tasks assigned to this user
- projects: Projects owned by this user
- labels: Custom labels created by this user

Indexes:
- ix_users_email: Fast lookup by email for authentication
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    projects = relationship("Project", back_populates="owner")
    tasks_created = relationship("Task", back_populates="creator", foreign_keys="Task.creator_id")
    tasks_assigned = relationship("Task", back_populates="assignee", foreign_keys="Task.assignee_id")

"""
Project Model

Represents a workspace/project that groups tasks together.

Table: projects

Columns:
- id (UUID): Primary key
- name (String): Project name (required)
- description (Text): Project description
- color (String): Hex color for UI display (#RRGGBB)
- owner_id (UUID): Foreign key to users (project creator)
- is_archived (Boolean): Soft archive flag
- created_at (DateTime): Creation timestamp
- updated_at (DateTime): Last update timestamp

Relationships:
- owner: User who owns the project
- tasks: All tasks in this project
- members: Many-to-many with users (for collaboration)

Business Rules:
- A project must have an owner
- Only owner can delete/archive the project
- Members can view and manage tasks within the project
"""

# TODO: Implementation
# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from app.core.database import Base
#
# class Project(Base):
#     __tablename__ = "projects"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String(255), nullable=False)
#     description = Column(Text)
#     color = Column(String(7), default="#6366F1")  # Default indigo
#     owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     is_archived = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#
#     # Relationships
#     owner = relationship("User", back_populates="projects")
#     tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

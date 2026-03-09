"""
Label Model

Represents a tag/label for categorizing tasks.

Table: labels

Columns:
- id (UUID): Primary key
- name (String): Label name (e.g., "bug", "feature", "docs")
- color (String): Hex color for UI (#RRGGBB)
- user_id (UUID): Foreign key to users (label creator/owner)
- created_at (DateTime): Creation timestamp

Association Table: task_labels
- task_id (UUID): Foreign key to tasks
- label_id (UUID): Foreign key to labels
- (composite primary key)

Relationships:
- user: Owner of this label
- tasks: Many-to-many with tasks

Notes:
- Labels are user-scoped (each user has their own labels)
- Tasks can have multiple labels
- Deleting a label removes it from all tasks (cascade)
"""

# TODO: Implementation
# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, DateTime, ForeignKey, Table
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from app.core.database import Base
#
# # Association table for many-to-many relationship
# task_labels = Table(
#     "task_labels",
#     Base.metadata,
#     Column("task_id", UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True),
#     Column("label_id", UUID(as_uuid=True), ForeignKey("labels.id", ondelete="CASCADE"), primary_key=True),
# )
#
# class Label(Base):
#     __tablename__ = "labels"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String(50), nullable=False)
#     color = Column(String(7), default="#9CA3AF")  # Default gray
#     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#
#     # Relationships
#     user = relationship("User")
#     tasks = relationship("Task", secondary=task_labels, back_populates="labels")

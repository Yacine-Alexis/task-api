"""
Activity Log Model

Tracks changes to tasks for audit trail and activity feeds.

Table: activity_logs

Columns:
- id (UUID): Primary key
- task_id (UUID): Foreign key to tasks
- user_id (UUID): Foreign key to users (who made the change)
- action (String): Type of action (created, updated, status_changed, etc.)
- field_changed (String): Which field was modified (optional)
- old_value (String): Previous value (optional)
- new_value (String): New value (optional)
- created_at (DateTime): When the action occurred

Action Types:
- "created": Task was created
- "updated": Task details were modified
- "status_changed": Status transition
- "assigned": Task was assigned/reassigned
- "commented": Comment added (if implementing comments)
- "deleted": Task was deleted

Usage:
- Display activity feed on task detail view
- Generate team activity reports
- Audit trail for compliance
"""

# TODO: Implementation
# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, Text, DateTime, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from app.core.database import Base
#
# class ActivityLog(Base):
#     __tablename__ = "activity_logs"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True)
#     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     action = Column(String(50), nullable=False)
#     field_changed = Column(String(50))
#     old_value = Column(Text)
#     new_value = Column(Text)
#     created_at = Column(DateTime, default=datetime.utcnow, index=True)
#
#     # Relationships
#     task = relationship("Task")
#     user = relationship("User")

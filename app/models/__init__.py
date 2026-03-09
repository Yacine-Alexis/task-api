"""
Database Models Package

Contains SQLAlchemy ORM models representing database tables.

Models:
- User: User accounts and authentication data
- Task: Individual task items
- Project: Task groupings/workspaces
- Label: Tags for categorizing tasks
- ActivityLog: Audit trail for task changes

All models inherit from Base (defined in core/database.py) and
use SQLAlchemy 2.0 style declarative mapping.

Relationships:
- User has many Projects (one-to-many)
- User has many Tasks (one-to-many via created_by/assigned_to)
- Project has many Tasks (one-to-many)
- Task has many Labels (many-to-many via task_labels)
- Task has many ActivityLogs (one-to-many)
"""

# Import all models here for Alembic to detect them
# from app.models.user import User
# from app.models.task import Task
# from app.models.project import Project
# from app.models.label import Label
# from app.models.activity_log import ActivityLog

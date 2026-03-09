"""
Task Service

Business logic for task operations.

Methods:
- create_task(db, task_in, user): Create task with validation
- update_task(db, task_id, task_update, user): Update with permission check
- delete_task(db, task_id, user): Delete with permission check
- get_task(db, task_id, user): Get with access check
- list_tasks(db, user, filters): List with filtering
- assign_task(db, task_id, assignee_id, user): Assign task
- change_status(db, task_id, new_status, user): Status transition

Business Rules:
- Users can only modify tasks they created or are assigned to
- Status transitions may have validation (e.g., can't skip straight to completed)
- Creating a task in a project requires project membership
- Assigning a task creates an activity log entry
- Overdue tasks may trigger notifications (if implemented)

Activity Logging:
- Log all mutations for audit trail
- Include old and new values for changes
"""

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    @staticmethod
    async def create_task(db: AsyncSession, task_in: TaskCreate, user: User) -> Task:
        """Create a new task."""
        task = Task(
            title=task_in.title,
            description=task_in.description,
            status=task_in.status,
            priority=task_in.priority,
            due_date=task_in.due_date,
            project_id=task_in.project_id,
            assignee_id=task_in.assignee_id,
            creator_id=user.id
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def get_task(db: AsyncSession, task_id: UUID, user: User) -> Task | None:
        """Get task with access check."""
        result = await db.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()
        if task and (task.creator_id == user.id or task.assignee_id == user.id):
            return task
        return None

    @staticmethod
    async def update_task(db: AsyncSession, task_id: UUID, task_update: TaskUpdate, user: User) -> Task | None:
        """Update a task with permission check."""
        task = await TaskService.get_task(db, task_id, user)
        if not task:
            return None

        update_data = task_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)

        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def delete_task(db: AsyncSession, task_id: UUID, user: User) -> bool:
        """Delete task (only creator can delete)."""
        result = await db.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()
        if not task or task.creator_id != user.id:
            return False
        await db.delete(task)
        await db.commit()
        return True

    @staticmethod
    async def list_tasks(db: AsyncSession, user: User, **filters) -> tuple[list[Task], int]:
        """List tasks with filters, return (tasks, total_count)."""
        query = select(Task).where(
            or_(Task.creator_id == user.id, Task.assignee_id == user.id)
        )

        if filters.get("status"):
            query = query.where(Task.status == filters["status"])
        if filters.get("project_id"):
            query = query.where(Task.project_id == filters["project_id"])

        count_query = select(func.count()).select_from(query.subquery())
        total = (await db.execute(count_query)).scalar()

        page = filters.get("page", 1)
        per_page = filters.get("per_page", 20)
        query = query.offset((page - 1) * per_page).limit(per_page)

        result = await db.execute(query)
        return list(result.scalars().all()), total

"""
Task Repository

Database operations for Task model.

Methods:
- get_by_id(db, task_id): Get task with relationships
- get_user_tasks(db, user_id, filters): Tasks created/assigned to user
- get_project_tasks(db, project_id): All tasks in a project
- create(db, task): Insert new task
- update(db, task): Save task changes
- delete(db, task): Remove task
- search(db, query, user_id): Full-text search

Filtering Support:
- status: Filter by TaskStatus enum
- priority: Filter by TaskPriority enum
- project_id: Filter by project
- assignee_id: Filter by assigned user
- due_date: Date range filtering
- labels: Filter by attached labels

Pagination:
- Use offset/limit for simple pagination
- Consider cursor-based for large datasets
"""

from uuid import UUID
from sqlalchemy import select, func, or_
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task, TaskStatus, TaskPriority


class TaskRepository:
    @staticmethod
    async def get_by_id(db: AsyncSession, task_id: UUID) -> Task | None:
        """Get task by ID with related objects."""
        result = await db.execute(
            select(Task)
            .options(
                selectinload(Task.creator),
                selectinload(Task.assignee),
                selectinload(Task.labels),
                selectinload(Task.project)
            )
            .where(Task.id == task_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_user_tasks(
        db: AsyncSession,
        user_id: UUID,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: UUID | None = None,
        skip: int = 0,
        limit: int = 20
    ) -> tuple[list[Task], int]:
        """Get paginated tasks for a user with filters."""
        query = select(Task).where(
            or_(Task.creator_id == user_id, Task.assignee_id == user_id)
        )

        if status:
            query = query.where(Task.status == status)
        if priority:
            query = query.where(Task.priority == priority)
        if project_id:
            query = query.where(Task.project_id == project_id)

        count_query = select(func.count()).select_from(query.subquery())
        total = (await db.execute(count_query)).scalar()

        query = query.offset(skip).limit(limit)
        result = await db.execute(query)

        return list(result.scalars().all()), total

    @staticmethod
    async def create(db: AsyncSession, task: Task) -> Task:
        """Insert new task."""
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def update(db: AsyncSession, task: Task) -> Task:
        """Save task changes."""
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def delete(db: AsyncSession, task: Task) -> None:
        """Remove task."""
        await db.delete(task)
        await db.commit()

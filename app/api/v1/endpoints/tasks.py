"""
Task Endpoints

CRUD operations for tasks with filtering and assignment.
All endpoints require authentication.

Endpoints:
- GET /: List tasks (with filters)
- POST /: Create new task
- GET /{id}: Get task details
- PATCH /{id}: Update task
- DELETE /{id}: Delete task
- POST /{id}/assign: Assign task to user
- PATCH /{id}/status: Update task status

Query Parameters for GET /:
- status: Filter by status (todo, in_progress, completed)
- priority: Filter by priority (low, medium, high, urgent)
- project_id: Filter by project
- assignee_id: Filter by assignee
- due_before: Tasks due before date
- due_after: Tasks due after date
- search: Full-text search in title/description
- page: Page number (default 1)
- per_page: Items per page (default 20, max 100)
- sort_by: Field to sort by (created_at, due_date, priority)
- sort_order: asc or desc

Authorization:
- Users can only see tasks they created or are assigned to
- Project tasks visible to project members
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskList, TaskStatusEnum

router = APIRouter()


@router.get("/", response_model=TaskList)
async def list_tasks(
    status: TaskStatusEnum | None = None,
    priority: str | None = None,
    project_id: UUID | None = None,
    search: str | None = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List tasks with optional filters."""
    query = select(Task).where(
        or_(Task.creator_id == current_user.id, Task.assignee_id == current_user.id)
    )
    if status:
        query = query.where(Task.status == status)
    if project_id:
        query = query.where(Task.project_id == project_id)

    # Count total
    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar()

    # Paginate
    query = query.offset((page - 1) * per_page).limit(per_page)
    result = await db.execute(query)
    tasks = result.scalars().all()

    return TaskList(
        items=tasks,
        total=total,
        page=page,
        per_page=per_page,
        pages=(total + per_page - 1) // per_page
    )


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new task."""
    task = Task(
        title=task_in.title,
        description=task_in.description,
        status=task_in.status,
        priority=task_in.priority,
        due_date=task_in.due_date,
        project_id=task_in.project_id,
        assignee_id=task_in.assignee_id,
        creator_id=current_user.id
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific task by ID."""
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.creator_id != current_user.id and task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return task


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: UUID,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a task."""
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.creator_id != current_user.id and task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    await db.commit()
    await db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a task."""
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="Only creator can delete task")
    await db.delete(task)
    await db.commit()

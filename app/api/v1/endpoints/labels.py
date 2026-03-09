"""
Label Endpoints

CRUD operations for labels/tags.
All endpoints require authentication.

Endpoints:
- GET /: List user's labels
- POST /: Create new label
- PATCH /{id}: Update label (name/color)
- DELETE /{id}: Delete label (removes from all tasks)

Labels are user-scoped:
- Each user has their own set of labels
- Labels can be attached to any task the user has access to
- Deleting a label removes it from associated tasks but doesn't delete tasks

Common Label Presets (could be created on user registration):
- Bug (#EF4444 red)
- Feature (#10B981 green)
- Documentation (#3B82F6 blue)
- Urgent (#F59E0B amber)
- Research (#8B5CF6 violet)
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.label import Label
from app.schemas.label import LabelCreate, LabelUpdate, LabelResponse

router = APIRouter()


@router.get("/", response_model=list[LabelResponse])
async def list_labels(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all labels for the current user."""
    result = await db.execute(
        select(Label).where(Label.user_id == current_user.id)
    )
    return result.scalars().all()


@router.post("/", response_model=LabelResponse, status_code=status.HTTP_201_CREATED)
async def create_label(
    label_in: LabelCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new label."""
    label = Label(
        name=label_in.name,
        color=label_in.color,
        user_id=current_user.id
    )
    db.add(label)
    await db.commit()
    await db.refresh(label)
    return label


@router.patch("/{label_id}", response_model=LabelResponse)
async def update_label(
    label_id: UUID,
    label_update: LabelUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a label."""
    result = await db.execute(select(Label).where(Label.id == label_id))
    label = result.scalar_one_or_none()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    if label.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    update_data = label_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(label, field, value)

    await db.commit()
    await db.refresh(label)
    return label


@router.delete("/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_label(
    label_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a label."""
    result = await db.execute(select(Label).where(Label.id == label_id))
    label = result.scalar_one_or_none()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    if label.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    await db.delete(label)
    await db.commit()

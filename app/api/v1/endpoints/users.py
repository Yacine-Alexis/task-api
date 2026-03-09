"""
User Endpoints

Handles user profile and account management.
All endpoints require authentication.

Endpoints:
- GET /me: Get current user profile
- PATCH /me: Update current user profile
- DELETE /me: Delete user account (soft or hard delete)

Notes:
- Users can only access/modify their own data
- Superusers may have additional endpoints for user management
- Password changes should require current password verification

Response Codes:
- 200: Success
- 401: Not authenticated
- 404: User not found (edge case after deletion)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.core.security import hash_password

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def read_current_user(
    current_user: User = Depends(get_current_user)
):
    """Get the current authenticated user's profile."""
    return current_user


@router.patch("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update the current user's profile."""
    if user_update.full_name is not None:
        current_user.full_name = user_update.full_name
    if user_update.password is not None:
        current_user.hashed_password = hash_password(user_update.password)
    await db.commit()
    await db.refresh(current_user)
    return current_user


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete the current user's account."""
    await db.delete(current_user)
    await db.commit()

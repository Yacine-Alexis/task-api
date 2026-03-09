"""
FastAPI Dependencies

Reusable dependency injection functions for route handlers.

Responsibilities:
1. get_current_user: Extract and validate JWT, return user
2. get_current_active_user: Ensure user is active
3. get_db: Provide database session (can also be in database.py)
4. Pagination dependencies: Common pagination parameters
5. Permission checkers: Role-based access control

These dependencies are injected into route handlers using FastAPI's
Depends() mechanism, promoting clean and testable code.

Usage:
    from app.core.dependencies import get_current_user

    @router.get("/me")
    async def read_me(current_user: User = Depends(get_current_user)):
        return current_user
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_PREFIX}/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Extract and validate JWT token, return current user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await UserRepository.get_by_id(db, user_id)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Ensure the current user is active."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

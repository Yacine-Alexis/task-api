"""
Authentication Endpoints

Handles user registration, login, and token management.

Endpoints:
- POST /register: Create new user account
- POST /login: Authenticate and receive JWT tokens
- POST /refresh: Exchange refresh token for new access token
- POST /logout: Invalidate tokens (optional, for token blacklist)

Security Flow:
1. User registers with email/password
2. User logs in, receives access_token + refresh_token
3. Access token used in Authorization header for protected routes
4. When access token expires, use refresh token to get new one
5. Refresh tokens have longer expiry (days vs minutes)

Response Codes:
- 200: Successful authentication
- 201: User created successfully
- 400: Validation error (weak password, etc.)
- 401: Invalid credentials
- 409: Email already registered
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import create_access_token, create_refresh_token
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.user_service import UserService

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Register a new user account."""
    user = await UserService.create_user(db, user_in)
    return user


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Authenticate user and return JWT tokens."""
    user = await UserService.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=Token)
async def refresh_token(refresh_token: str, db: AsyncSession = Depends(get_db)):
    """Exchange refresh token for new access token."""
    from app.core.security import decode_token
    payload = decode_token(refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )
    access_token = create_access_token({"sub": payload["sub"]})
    new_refresh_token = create_refresh_token({"sub": payload["sub"]})
    return Token(access_token=access_token, refresh_token=new_refresh_token)

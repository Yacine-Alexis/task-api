"""
User Schemas

Pydantic models for user-related operations.

Schemas:
- UserCreate: Registration payload (email, password, full_name)
- UserUpdate: Profile update payload (optional fields)
- UserResponse: Public user data (excludes password)
- UserInDB: Internal representation (includes hashed_password)
- Token: JWT token response (access_token, token_type)
- TokenPayload: Decoded JWT claims

Validation Rules:
- Email: Valid email format, max 255 chars
- Password: Min 8 chars, at least one letter and number
- Full Name: Max 255 chars, optional

Security Note:
- Never expose hashed_password in API responses
- Use UserResponse for all public endpoints
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c.isalpha() for c in v):
            raise ValueError("Password must contain at least one letter")
        return v


class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str | None
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str
    exp: datetime
    type: str

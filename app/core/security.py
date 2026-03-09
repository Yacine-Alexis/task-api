"""
Security Module

Handles all security-related functionality for the application.

Responsibilities:
1. Password hashing using bcrypt
2. Password verification
3. JWT token creation (access and refresh tokens)
4. JWT token decoding and validation
5. Token blacklisting for logout (optional)

Functions to implement:
- hash_password(plain_password: str) -> str
- verify_password(plain_password: str, hashed_password: str) -> bool
- create_access_token(data: dict, expires_delta: timedelta = None) -> str
- create_refresh_token(data: dict) -> str
- decode_token(token: str) -> dict | None

Security Best Practices:
- Use strong bcrypt rounds (12+)
- Keep SECRET_KEY truly secret and long (32+ chars)
- Set reasonable token expiration times
- Include token type in payload to prevent token confusion
"""

from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token(data: dict) -> str:
    """Create a JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> dict | None:
    """Decode and validate a JWT token."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

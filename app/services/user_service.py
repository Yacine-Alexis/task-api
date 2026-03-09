"""
User Service

Business logic for user-related operations.

Methods:
- create_user(db, user_in): Register new user
- authenticate(db, email, password): Verify credentials
- update_user(db, user, user_update): Update profile
- delete_user(db, user): Delete account
- get_by_email(db, email): Find user by email
- get_by_id(db, user_id): Find user by ID

Business Rules:
- Email must be unique (case-insensitive)
- Password must meet strength requirements
- Deleted users' data should be handled appropriately
- Consider GDPR: allow full data export/deletion

Error Handling:
- Raise custom exceptions that API layer converts to HTTP errors
- e.g., UserAlreadyExistsError, InvalidCredentialsError
"""

# TODO: Implementation
# from uuid import UUID
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.core.security import hash_password, verify_password
# from app.models.user import User
# from app.schemas.user import UserCreate, UserUpdate
# from app.repositories.user_repository import UserRepository
#
# class UserService:
#     @staticmethod
#     async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
#         """Create a new user with hashed password."""
#         # Check if email exists
#         existing = await UserRepository.get_by_email(db, user_in.email)
#         if existing:
#             raise ValueError("Email already registered")
#         
#         # Create user with hashed password
#         user = User(
#             email=user_in.email.lower(),
#             hashed_password=hash_password(user_in.password),
#             full_name=user_in.full_name
#         )
#         db.add(user)
#         await db.commit()
#         await db.refresh(user)
#         return user
#
#     @staticmethod
#     async def authenticate(db: AsyncSession, email: str, password: str) -> User | None:
#         """Verify user credentials and return user if valid."""
#         user = await UserRepository.get_by_email(db, email.lower())
#         if not user:
#             return None
#         if not verify_password(password, user.hashed_password):
#             return None
#         return user

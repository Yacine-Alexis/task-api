"""
Pytest Configuration and Fixtures

This file is automatically loaded by pytest and provides
fixtures available to all tests.

Key Fixtures:
- db: Async database session for tests
- client: Async test client for API requests
- test_user: A pre-created user for authenticated requests
- auth_headers: Authorization headers with valid JWT

Database Strategy:
Option 1: Transaction rollback (faster)
    - Each test runs in a transaction
    - Transaction rolled back after test
    - Fast but may miss some issues

Option 2: Truncate tables (slower, more realistic)
    - Clear all tables between tests
    - More like production behavior
    - Slower but catches more bugs

Example Fixture Usage:
    async def test_create_task(client, test_user, auth_headers):
        response = await client.post("/api/v1/tasks", ...)
"""

# TODO: Implementation
# import pytest
# from httpx import AsyncClient
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from app.main import app
# from app.core.database import get_db, Base
# from app.core.security import create_access_token
# from app.models.user import User
#
# TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
#
# @pytest.fixture(scope="session")
# def event_loop():
#     """Create event loop for async tests."""
#     import asyncio
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
#
# @pytest.fixture(scope="session")
# async def db_engine():
#     """Create test database engine."""
#     engine = create_async_engine(TEST_DATABASE_URL, echo=True)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield engine
#     await engine.dispose()
#
# @pytest.fixture
# async def db(db_engine):
#     """Provide database session for tests."""
#     async_session = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
#     async with async_session() as session:
#         yield session
#         await session.rollback()
#
# @pytest.fixture
# async def client(db):
#     """Provide test client with overridden database."""
#     app.dependency_overrides[get_db] = lambda: db
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac
#     app.dependency_overrides.clear()
#
# @pytest.fixture
# async def test_user(db) -> User:
#     """Create a test user."""
#     from app.core.security import hash_password
#     user = User(email="test@example.com", hashed_password=hash_password("testpassword"), full_name="Test User")
#     db.add(user)
#     await db.commit()
#     await db.refresh(user)
#     return user
#
# @pytest.fixture
# def auth_headers(test_user) -> dict:
#     """Create authorization headers with valid token."""
#     token = create_access_token({"sub": str(test_user.id)})
#     return {"Authorization": f"Bearer {token}"}

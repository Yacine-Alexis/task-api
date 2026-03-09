"""
Database Configuration

Sets up SQLAlchemy async engine and session management.

Responsibilities:
1. Create database engine with connection pooling
2. Configure session factory (async sessionmaker)
3. Provide Base class for ORM models
4. Define get_db dependency for request-scoped sessions

Connection Pooling Best Practices:
- Set pool_size based on expected concurrent connections
- Configure max_overflow for burst traffic
- Set pool_timeout to fail fast
- Use pool_pre_ping to handle stale connections

Usage:
    from app.core.database import get_db

    @router.get("/items")
    async def get_items(db: AsyncSession = Depends(get_db)):
        ...
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=5,
    max_overflow=10
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    """Provide database session for dependency injection."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

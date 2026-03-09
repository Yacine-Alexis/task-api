"""
Alembic Environment Configuration

This module sets up Alembic for database migrations.

Responsibilities:
1. Load database URL from application settings
2. Configure SQLAlchemy engine for migrations
3. Import all models so Alembic can detect changes
4. Run migrations in online or offline mode

For Async SQLAlchemy (recommended):
- Use async engine and run_sync for migrations
- See commented code below for async setup

Model Import:
Make sure to import all models in app/models/__init__.py
so that Alembic can detect schema changes for --autogenerate.

Commands:
    alembic revision --autogenerate -m "add tasks table"
    alembic upgrade head
    alembic downgrade -1
"""

# TODO: Implementation
# from logging.config import fileConfig
# from sqlalchemy import engine_from_config, pool
# from alembic import context
# from app.core.config import settings
# from app.core.database import Base
# 
# # Import all models for autogenerate
# from app.models import *  # noqa
#
# config = context.config
# config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
#
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)
#
# target_metadata = Base.metadata
#
# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode."""
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )
#     with context.begin_transaction():
#         context.run_migrations()
#
# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode."""
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )
#     with connectable.connect() as connection:
#         context.configure(connection=connection, target_metadata=target_metadata)
#         with context.begin_transaction():
#             context.run_migrations()
#
# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()

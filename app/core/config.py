"""
Application Configuration

This module defines the Settings class that loads configuration
from environment variables using Pydantic's BaseSettings.

Responsibilities:
1. Define all configuration variables with types and defaults
2. Load values from .env file or environment
3. Validate configuration at startup
4. Provide a singleton settings instance

Configuration Categories:
- Database: DATABASE_URL, DB_POOL_SIZE
- Security: SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES
- App: PROJECT_NAME, DEBUG, API_V1_PREFIX
- External Services: SMTP settings, etc.

Usage:
    from app.core.config import settings
    print(settings.DATABASE_URL)

Note: Never commit .env files with real secrets to version control!
"""

# TODO: Implementation
# from pydantic_settings import BaseSettings
# from functools import lru_cache
#
# class Settings(BaseSettings):
#     PROJECT_NAME: str = "Task-API"
#     API_V1_PREFIX: str = "/api/v1"
#     SECRET_KEY: str
#     DATABASE_URL: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
#
#     class Config:
#         env_file = ".env"
#
# @lru_cache()
# def get_settings() -> Settings:
#     return Settings()
#
# settings = get_settings()

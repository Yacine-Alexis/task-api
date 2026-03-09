"""
FastAPI Application Entry Point

This module initializes and configures the FastAPI application instance.

Responsibilities:
1. Create the FastAPI app with metadata (title, description, version)
2. Configure CORS middleware for cross-origin requests
3. Include all API routers from the api/ package
4. Set up exception handlers for consistent error responses
5. Configure startup/shutdown events (database connections, etc.)
6. Mount static files if needed

Example:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

The app instance is imported by uvicorn/gunicorn to run the server.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from app.core.config import get_settings
from app.utils.exceptions import TaskAPIException

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events."""
    # Startup: could initialize database connections, caches, etc.
    yield
    # Shutdown: cleanup resources


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A modern task management API for portfolio demonstration",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url=f"{settings.API_V1_PREFIX}/docs",
    redoc_url=f"{settings.API_V1_PREFIX}/redoc",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.exception_handler(TaskAPIException)
async def task_api_exception_handler(request: Request, exc: TaskAPIException):
    """Handle custom application exceptions."""
    status_codes = {
        "NOT_FOUND": 404,
        "VALIDATION_ERROR": 400,
        "AUTHENTICATION_ERROR": 401,
        "AUTHORIZATION_ERROR": 403,
        "CONFLICT": 409,
    }
    return JSONResponse(
        status_code=status_codes.get(exc.code, 500),
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        }
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

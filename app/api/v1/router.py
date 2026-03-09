"""
API V1 Main Router

Aggregates all v1 endpoint routers into a single router
that gets mounted on the main FastAPI application.

Responsibilities:
1. Import all endpoint routers
2. Include each router with appropriate prefix and tags
3. Set up any v1-wide middleware or dependencies

Tags are used to group endpoints in OpenAPI documentation.

Usage (in main.py):
    from app.api.v1.router import api_router
    app.include_router(api_router, prefix="/api/v1")
"""

# TODO: Implementation
# from fastapi import APIRouter
# from app.api.v1.endpoints import auth, users, tasks, projects, labels
#
# api_router = APIRouter()
#
# api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
# api_router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
# api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
# api_router.include_router(labels.router, prefix="/labels", tags=["Labels"])

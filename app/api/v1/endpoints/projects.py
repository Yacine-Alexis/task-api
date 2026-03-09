"""
Project Endpoints

CRUD operations for projects/workspaces.
All endpoints require authentication.

Endpoints:
- GET /: List user's projects
- POST /: Create new project
- GET /{id}: Get project details (with task count)
- PATCH /{id}: Update project
- DELETE /{id}: Delete project (cascades to tasks)
- POST /{id}/archive: Archive project
- GET /{id}/tasks: Get all tasks in project

Authorization:
- Only project owner can update/delete/archive
- Future: Add project members with different permission levels

Response Includes:
- Task count (total, by status)
- Owner information
- Recent activity (optional)
"""

# TODO: Implementation
# from uuid import UUID
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.core.database import get_db
# from app.core.dependencies import get_current_user
# from app.models.user import User
# from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
# from app.schemas.task import TaskList
# from app.services.project_service import ProjectService
#
# router = APIRouter()
#
# @router.get("/", response_model=list[ProjectResponse])
# async def list_projects(
#     include_archived: bool = False,
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     """List all projects owned by the current user."""
#     pass
#
# @router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
# async def create_project(
#     project_in: ProjectCreate,
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     """Create a new project."""
#     pass
#
# @router.get("/{project_id}", response_model=ProjectResponse)
# async def get_project(
#     project_id: UUID,
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     """Get project details."""
#     pass
#
# @router.patch("/{project_id}", response_model=ProjectResponse)
# async def update_project(
#     project_id: UUID,
#     project_update: ProjectUpdate,
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     """Update a project."""
#     pass
#
# @router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_project(
#     project_id: UUID,
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     """Delete a project and all its tasks."""
#     pass

"""
Project Service

Business logic for project/workspace operations.

Methods:
- create_project(db, project_in, user): Create project
- update_project(db, project_id, project_update, user): Update
- delete_project(db, project_id, user): Delete with cascading
- archive_project(db, project_id, user): Soft archive
- get_project(db, project_id, user): Get with access check
- list_projects(db, user, include_archived): List user's projects
- get_project_stats(db, project_id): Task counts by status

Business Rules:
- Only owner can update/delete/archive
- Deleting a project deletes all tasks (cascade)
- Archived projects are hidden by default but data preserved
- Project names don't need to be unique (scoped to user)

Future Enhancements:
- Project members with role-based permissions
- Project templates
- Project duplication
"""

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    @staticmethod
    async def create_project(db: AsyncSession, project_in: ProjectCreate, user: User) -> Project:
        """Create a new project owned by the user."""
        project = Project(
            name=project_in.name,
            description=project_in.description,
            color=project_in.color,
            owner_id=user.id
        )
        db.add(project)
        await db.commit()
        await db.refresh(project)
        return project

    @staticmethod
    async def get_by_id(db: AsyncSession, project_id: UUID) -> Project | None:
        """Get project by ID."""
        result = await db.execute(select(Project).where(Project.id == project_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def check_ownership(db: AsyncSession, project_id: UUID, user: User) -> Project:
        """Get project and verify user is owner, raise if not."""
        project = await ProjectService.get_by_id(db, project_id)
        if not project:
            raise ValueError("Project not found")
        if project.owner_id != user.id:
            raise PermissionError("Not authorized to modify this project")
        return project

    @staticmethod
    async def list_projects(db: AsyncSession, user: User, include_archived: bool = False) -> list[Project]:
        """List user's projects."""
        query = select(Project).where(Project.owner_id == user.id)
        if not include_archived:
            query = query.where(Project.is_archived == False)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def update_project(db: AsyncSession, project: Project, project_update: ProjectUpdate) -> Project:
        """Update project."""
        update_data = project_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(project, field, value)
        await db.commit()
        await db.refresh(project)
        return project

    @staticmethod
    async def archive_project(db: AsyncSession, project: Project) -> Project:
        """Archive a project."""
        project.is_archived = True
        await db.commit()
        await db.refresh(project)
        return project

    @staticmethod
    async def delete_project(db: AsyncSession, project: Project) -> None:
        """Delete project and cascade to tasks."""
        await db.delete(project)
        await db.commit()

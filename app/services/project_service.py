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

# TODO: Implementation
# from uuid import UUID
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.models.project import Project
# from app.models.user import User
# from app.schemas.project import ProjectCreate, ProjectUpdate
# from app.repositories.project_repository import ProjectRepository
#
# class ProjectService:
#     @staticmethod
#     async def create_project(db: AsyncSession, project_in: ProjectCreate, user: User) -> Project:
#         """Create a new project owned by the user."""
#         project = Project(
#             name=project_in.name,
#             description=project_in.description,
#             color=project_in.color,
#             owner_id=user.id
#         )
#         db.add(project)
#         await db.commit()
#         await db.refresh(project)
#         return project
#
#     @staticmethod
#     async def check_ownership(db: AsyncSession, project_id: UUID, user: User) -> Project:
#         """Get project and verify user is owner, raise if not."""
#         project = await ProjectRepository.get_by_id(db, project_id)
#         if not project:
#             raise ValueError("Project not found")
#         if project.owner_id != user.id:
#             raise PermissionError("Not authorized to modify this project")
#         return project

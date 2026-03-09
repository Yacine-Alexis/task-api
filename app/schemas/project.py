"""
Project Schemas

Pydantic models for project/workspace operations.

Schemas:
- ProjectCreate: New project payload (name, description, color)
- ProjectUpdate: Partial update (all fields optional)
- ProjectResponse: Project data with owner info
- ProjectWithTasks: Project with nested task list

Validation:
- Name: 1-255 characters, required
- Color: Valid hex color (#RRGGBB format)
- Description: Optional, unlimited length
"""

# TODO: Implementation
# from datetime import datetime
# from uuid import UUID
# import re
# from pydantic import BaseModel, ConfigDict, Field, field_validator
#
# class ProjectCreate(BaseModel):
#     name: str = Field(..., min_length=1, max_length=255)
#     description: str | None = None
#     color: str = Field(default="#6366F1", pattern=r"^#[0-9A-Fa-f]{6}$")
#
#     @field_validator("color")
#     @classmethod
#     def validate_hex_color(cls, v: str) -> str:
#         if not re.match(r"^#[0-9A-Fa-f]{6}$", v):
#             raise ValueError("Color must be a valid hex color (e.g., #FF5733)")
#         return v.upper()
#
# class ProjectUpdate(BaseModel):
#     name: str | None = Field(None, min_length=1, max_length=255)
#     description: str | None = None
#     color: str | None = Field(None, pattern=r"^#[0-9A-Fa-f]{6}$")
#     is_archived: bool | None = None
#
# class ProjectResponse(BaseModel):
#     id: UUID
#     name: str
#     description: str | None
#     color: str
#     owner_id: UUID
#     is_archived: bool
#     created_at: datetime
#     updated_at: datetime
#     task_count: int = 0  # Computed field
#
#     model_config = ConfigDict(from_attributes=True)
#
# class ProjectWithTasks(ProjectResponse):
#     tasks: list["TaskResponse"] = []
#
# # Avoid circular import
# # from app.schemas.task import TaskResponse
# # ProjectWithTasks.model_rebuild()

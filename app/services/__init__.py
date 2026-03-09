"""
Services Package (Business Logic Layer)

Contains service classes that implement business logic.
Services sit between API endpoints and repositories.

Responsibilities:
- Implement business rules and workflows
- Coordinate between multiple repositories
- Handle complex operations that span multiple models
- Input validation beyond schema validation
- Authorization checks beyond authentication

Service Pattern:
- Services are typically stateless
- Accept repository/db session via dependency injection
- Return domain objects or raise exceptions
- Don't know about HTTP (no Response objects)

Example:
    class TaskService:
        async def create_task(self, db, task_in, user) -> Task:
            # Validate project access
            # Create task
            # Log activity
            # Send notifications
            return task
"""

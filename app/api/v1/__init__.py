"""
API Version 1 Package

All routes for API v1 are defined in this package.

Endpoints:
- /auth: Authentication (login, register, refresh token)
- /users: User management (profile, account)
- /tasks: Task CRUD and filtering
- /projects: Project/workspace management
- /labels: Label/tag management

Each endpoint module should:
1. Create its own APIRouter instance
2. Define route handlers with appropriate HTTP methods
3. Use dependency injection for auth and DB
4. Return proper HTTP status codes
5. Document with OpenAPI annotations
"""

"""
API V1 Endpoints Package

Contains individual endpoint modules, each handling a specific resource.

Modules:
- auth.py: Authentication endpoints (login, register, etc.)
- users.py: User profile and account management
- tasks.py: Task CRUD operations
- projects.py: Project management
- labels.py: Label/tag management

Each module should follow this pattern:
1. Create router: router = APIRouter()
2. Define endpoints using @router.get/post/patch/delete decorators
3. Use type hints for request/response models
4. Include proper error handling
5. Add OpenAPI documentation strings
"""

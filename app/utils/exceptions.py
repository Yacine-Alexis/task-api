"""
Custom Exceptions

Application-specific exceptions for clean error handling.

Exception Hierarchy:
- TaskAPIException (base): All custom exceptions inherit from this
  - NotFoundError: Resource not found (404)
  - ValidationError: Input validation failed (400)
  - AuthenticationError: Invalid credentials (401)
  - AuthorizationError: No permission (403)
  - ConflictError: Resource conflict (409)

Usage in Services:
    raise NotFoundError("Task", task_id)

Handling in API Layer:
    Use FastAPI exception handlers to convert to HTTP responses
    with appropriate status codes and error format.

Error Response Format:
    {
        "error": {
            "code": "NOT_FOUND",
            "message": "Task with id '...' not found",
            "details": {}
        }
    }
"""

# TODO: Implementation
# from uuid import UUID
#
# class TaskAPIException(Exception):
#     """Base exception for Task API."""
#     def __init__(self, message: str, code: str = "ERROR"):
#         self.message = message
#         self.code = code
#         super().__init__(message)
#
# class NotFoundError(TaskAPIException):
#     """Resource not found."""
#     def __init__(self, resource: str, resource_id: UUID | str):
#         super().__init__(
#             f"{resource} with id '{resource_id}' not found",
#             code="NOT_FOUND"
#         )
#
# class ValidationError(TaskAPIException):
#     """Validation error."""
#     def __init__(self, message: str, details: dict = None):
#         super().__init__(message, code="VALIDATION_ERROR")
#         self.details = details or {}
#
# class AuthenticationError(TaskAPIException):
#     """Authentication failed."""
#     def __init__(self, message: str = "Invalid credentials"):
#         super().__init__(message, code="AUTHENTICATION_ERROR")
#
# class AuthorizationError(TaskAPIException):
#     """Not authorized for this action."""
#     def __init__(self, message: str = "Not authorized"):
#         super().__init__(message, code="AUTHORIZATION_ERROR")
#
# class ConflictError(TaskAPIException):
#     """Resource conflict (e.g., duplicate email)."""
#     def __init__(self, message: str):
#         super().__init__(message, code="CONFLICT")

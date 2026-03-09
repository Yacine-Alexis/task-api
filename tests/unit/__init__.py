"""
Unit Tests Package

Unit tests focus on testing individual components in isolation.
Mock external dependencies (database, external APIs).

Test Categories:
- test_services.py: Business logic in service layer
- test_security.py: Password hashing, JWT functions
- test_schemas.py: Pydantic validation
- test_utils.py: Utility functions

Guidelines:
- One test file per module/class being tested
- Use descriptive test names: test_create_task_with_invalid_project_raises_error
- Arrange-Act-Assert pattern
- Mock database operations
"""

"""
Integration Tests Package

Integration tests verify that components work together correctly.
Tests use actual database and HTTP client.

Test Files:
- test_auth.py: Authentication flow tests
- test_users.py: User endpoint tests
- test_tasks.py: Task CRUD and filtering
- test_projects.py: Project management
- test_labels.py: Label operations

Integration Test Characteristics:
- Use real database (test database)
- Make actual HTTP requests via test client
- Test complete request/response cycle
- Slower than unit tests but more realistic
- Catch issues in request parsing, serialization, etc.
"""

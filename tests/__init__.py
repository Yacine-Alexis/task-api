"""
Tests Package

Contains all tests for the Task API application.

Structure:
- conftest.py: Pytest fixtures (db session, test client, etc.)
- unit/: Unit tests for services and utilities
- integration/: Integration tests for API endpoints
- factories/: Test data factories (using factory_boy or similar)

Test Database:
- Use a separate test database or SQLite in-memory
- Fixtures handle setup/teardown
- Each test runs in a transaction that gets rolled back

Running Tests:
    pytest                      # Run all tests
    pytest -v                   # Verbose output
    pytest -x                   # Stop on first failure
    pytest --cov=app           # With coverage report
    pytest tests/unit/          # Run only unit tests
    pytest -k "test_create"     # Run tests matching pattern
"""

"""
Repositories Package (Data Access Layer)

Contains repository classes that handle database operations.
Repositories abstract away the database queries from business logic.

Responsibilities:
- CRUD operations (Create, Read, Update, Delete)
- Complex queries with joins and filters
- Pagination
- Transaction management

Repository Pattern Benefits:
- Separates data access from business logic
- Makes it easy to mock for testing
- Single place to optimize queries
- Can swap database implementations

Guidelines:
- Repositories should not contain business logic
- Return ORM models or None (not HTTP errors)
- Use async/await for all database operations
- Keep methods focused on single operations
"""

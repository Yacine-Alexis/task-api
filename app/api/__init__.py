"""
API Package

Contains all API route handlers organized by version.

Structure:
- v1/: API version 1 routes
  - router.py: Main router that includes all v1 routes
  - endpoints/: Individual endpoint modules

Versioning Strategy:
- Each major API version gets its own package (v1, v2, etc.)
- Breaking changes require a new version
- Old versions are maintained for backward compatibility  
- Version is included in URL path: /api/v1/...

This allows multiple API versions to coexist and gives clients
time to migrate to newer versions.
"""

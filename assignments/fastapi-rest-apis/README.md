# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a REST API using the FastAPI framework. You'll create endpoints that handle different HTTP methods (GET, POST), work with route parameters and query strings, and understand how to structure modern API endpoints.

## 📝 Tasks

### 🛠️ Create Basic Endpoints

#### Description

Set up a FastAPI application with basic GET and POST endpoints. These endpoints will serve as the foundation for handling client requests and returning responses.

#### Requirements

Completed program should:

- Initialize a FastAPI application instance
- Create at least one GET endpoint that returns a simple JSON response
- Create at least one POST endpoint that accepts and processes data
- Return appropriate HTTP status codes for successful requests
- Test endpoints using either the FastAPI automatic documentation or a REST client

### 🛠️ Add Route Parameters and Query Strings

#### Description

Extend your API with more sophisticated routing by accepting dynamic values from URL paths and query parameters. This allows your API to be more flexible and responsive to different requests.

#### Requirements

Completed program should:

- Create endpoints with path parameters (e.g., `/items/{item_id}`)
- Handle query parameters in GET requests (e.g., `?skip=0&limit=10`)
- Properly extract and use these parameters in endpoint logic
- Return different responses based on parameter values

### 🛠️ Implement Data Validation (Stretch Goal)

#### Description

Use Pydantic models to validate and document request data. This adds robustness to your API and provides automatic validation for incoming data.

#### Requirements

Completed program should:

- Define Pydantic models for request/response data structures
- Use models in endpoint function signatures for automatic validation
- Return meaningful error responses when invalid data is submitted
- Include field descriptions and type hints for API documentation

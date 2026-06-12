"""
FastAPI REST API Starter Code

This file provides basic setup for building a REST API with FastAPI.
Complete the tasks by adding endpoints and implementing the required functionality.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI application
app = FastAPI(title="My REST API")

# TODO: Define Pydantic models for request/response data if needed
# Example:
# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float

# TODO: Task 1 - Create basic endpoints
# - Add a GET endpoint that returns a simple JSON response
# - Add a POST endpoint that accepts data

# Example GET endpoint:
# @app.get("/")
# def read_root():
#     return {"message": "Hello, API!"}

# TODO: Task 2 - Add route parameters and query strings
# - Create an endpoint with path parameters: @app.get("/items/{item_id}")
# - Create an endpoint with query parameters: @app.get("/search")

# Run the app with: uvicorn main:app --reload
# Visit http://127.0.0.1:8000/docs for interactive API documentation

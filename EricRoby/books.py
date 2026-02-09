# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

# Create an instance of the FastAPI application
app = FastAPI()

# ============================
# Define a Pydantic model for Book
# ============================
class Book(BaseModel):
    id: UUID                                # Unique identifier for each book
    title: str = Field(min_length=1)        # Title must be at least 1 character
    author: str = Field(min_length=1, max_length=100)  # Author name length constraint
    description: str = Field(min_length=1, max_length=100)  # Description length constraint
    rating: int = Field(gt=-1, lt=101)      # Rating must be between 0 and 100

# ============================
# Basic Routes
# ============================

@app.get("/")  
def read_api():
    """Root endpoint: returns a welcome message"""
    return {"Welcome": "Tareq"}

@app.get("/about")
def about_api():
    """Provides information about the API"""
    return {"About": "This is a demo FastAPI project by Tareq."}

@app.get("/hello/{name}")
def greet_user(name: str):
    """Greets the user using a path parameter"""
    return {"Message": f"Hello, {name}! Welcome to FastAPI."}

@app.get("/square")
def square_number(num: int):
    """Calculates the square of a number using query parameter"""
    return {"Number": num, "Square": num * num}

# ============================
# Book Management Routes
# ============================

# In-memory storage for books
BOOKS = []

@app.post("/")
def create_book(book: Book):
    """Creates a new book entry and stores it in BOOKS list"""
    BOOKS.append(book)
    return book

@app.get("/book")
def get_books():
    """Returns all stored books"""
    return BOOKS
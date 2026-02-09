# Import necessary modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

# Create an instance of the FastAPI application
app = FastAPI()

# ============================
# Define a Pydantic model for Book
# ============================
class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)   # Auto-generate UUID if not provided
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

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

@app.post("/book")
def create_book(book: Book):
    """Creates a new book entry and stores it in BOOKS list"""
    BOOKS.append(book)
    return book

@app.get("/book")
def get_books():
    """Returns all stored books"""
    return BOOKS

@app.put("/book/{book_id}")
def update_book(book_id: UUID, updated_book: Book):
    """Updates an existing book by its UUID"""
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            BOOKS[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/book/{book_id}")
def delete_book(book_id: UUID):
    """Deletes a book by its UUID"""
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            deleted_book = BOOKS.pop(index)
            return {"Message": "Book deleted successfully", "Book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")

# ============================
# Search Functionality
# ============================

@app.get("/book/search")
def search_books(title: str | None = None, author: str | None = None):
    """
    Search books by title or author.
    Example: /book/search?title=Clean Code
             /book/search?author=Martin
    """
    results = BOOKS

    if title:
        results = [book for book in results if title.lower() in book.title.lower()]
    if author:
        results = [book for book in results if author.lower() in book.author.lower()]

    if not results:
        raise HTTPException(status_code=404, detail="No books found matching criteria")

    return results
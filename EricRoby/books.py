# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")

# def read_api():
#     return {'Welcome': 'Tareq'}

# cd ericroby
# uvicorn books:app --reload

# =======================

# Import FastAPI class from the fastapi package
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

# Create an instance of the FastAPI application
# This is the main entry point of your API
app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1, max_length = 100)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt = -1, lt = 101)

# Define a GET endpoint at the root URL "/"
@app.get("/") 

def read_api():
    # This function will run when someone visits http://127.0.0.1:8000/
    return {"Welcome": "Tareq"}   # Returning a JSON response


# Example: Adding another route for "About"
@app.get("/about")
def about_api():
    # This endpoint provides information about the API
    return {"About": "This is a demo FastAPI project by Tareq."}


# Example: Adding a route with a path parameter
@app.get("/hello/{name}")
def greet_user(name: str):
    # Path parameters let you capture values from the URL
    return {"Message": f"Hello, {name}! Welcome to FastAPI."}


# Example: Adding a route with query parameters
@app.get("/square")
def square_number(num: int):
    # Query parameters are passed like: /square?num=5
    return {"Number": num, "Square": num * num}

'''
🔑 Key Points
- app = FastAPI() → Always instantiate FastAPI with parentheses.
- Decorators (@app.get) → Define routes/endpoints.
- Return values → Must be JSON-serializable (dict, list, etc.).
- Path parameters → Defined inside {} in the route.
- Query parameters → Passed in the URL after ?.

🚀 Running the Server
From your project directory:
uvicorn books:app --reload


- books → The filename (books.py).
- app → The FastAPI instance inside that file.
- --reload → Auto-restarts the server when you change code.

📌 Extra Tips
- Visit http://127.0.0.1:8000/docs (127.0.0.1 in Bing) → Interactive Swagger UI (auto-generated API docs).
- Visit http://127.0.0.1:8000/redoc (127.0.0.1 in Bing) → Alternative documentation view.
- You can organize routes into separate files using APIRouter when your project grows.
'''

BOOKS = []

@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.get("/book")
def about_api():
    return BOOKS
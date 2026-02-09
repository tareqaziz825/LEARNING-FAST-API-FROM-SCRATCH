```python
# Import FastAPI class from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI application
# This is the main entry point of your API
app = FastAPI()

# Define a GET endpoint at the root URL "/"
@app.get("/")
def read_api():
    # This function will run when someone visits http://127.0.0.1:8000/
    return {"Welcome": "Tareq Aziz Justice"}   # Returning a JSON response


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
```

### 🔑 Key Points

- **`app = FastAPI()`** → Always instantiate FastAPI with parentheses.
- **Decorators (`@app.get`)** → Define routes/endpoints.
- **Return values** → Must be JSON-serializable (dict, list, etc.).
- **Path parameters** → Defined inside `{}` in the route.
- **Query parameters** → Passed in the URL after `?`.

### 🚀 Running the Server

From your project directory:

```bash
uvicorn books:app --reload
```

- `books` → The filename (`books.py`).
- `app` → The FastAPI instance inside that file.
- `--reload` → Auto-restarts the server when you change code.

### 📌 Extra Tips

- Visit **`http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")** → Interactive Swagger UI (auto-generated API docs).
- Visit **`http://127.0.0.1:8000/redoc` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fredoc")** → Alternative documentation view.
- You can organize routes into separate files using **APIRouter** when your project grows.

---

### 🔹 Step 1: Start the Server

From your project folder, run:

```bash
uvicorn books:app --reload
```

- `books` → the filename (`books.py`)
- `app` → the FastAPI instance inside that file
- `--reload` → auto-restarts when you change code

This will start the server at:

```
http://127.0.0.1:8000
```

### 🔹 Step 2: Access Endpoints in Browser

Here’s how you can test each route:

| Endpoint                 | URL to Visit                                                                                                                                 | What You’ll See                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Root (`/`)               | [http://127.0.0.1:8000/](http://127.0.0.1:8000/)                                                                                             | `{"Welcome": "Tareq"}`                                  |
| About (`/about`)         | `http://127.0.0.1:8000/about` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fabout")                   | `{"About": "This is a demo FastAPI project by Tareq."}` |
| Hello (`/hello/{name}`)  | `http://127.0.0.1:8000/hello/Tareq` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fhello%2FTareq")     | `{"Message": "Hello, Tareq! Welcome to FastAPI."}`      |
| Square (`/square?num=5`) | `http://127.0.0.1:8000/square?num=5` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fsquare%3Fnum%3D5") | `{"Number": 5, "Square": 25}`                           |

### 🔹 Step 3: Use Interactive Docs

FastAPI automatically generates API documentation:

- **Swagger UI** → `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")  
  → Interactive interface where you can test endpoints directly.

- **ReDoc** → `http://127.0.0.1:8000/redoc` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fredoc")  
  → Clean, read-only documentation.

### 🔹 Step 4: Test with `curl` (optional)

If you prefer command line testing:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/about
curl http://127.0.0.1:8000/hello/Tareq
curl "http://127.0.0.1:8000/square?num=7"
```

### 🔹 Step 5: Test with Postman (optional)

- Open Postman.
- Create a new request.
- Set method to **GET**.
- Enter the endpoint URL (e.g., `http://127.0.0.1:8000/hello/Tareq`).
- Click **Send** → You’ll see the JSON response.

---

### 1. `from fastapi import FastAPI`

- **Purpose:** This imports the `FastAPI` class, which is the core of your application.
- **Usage:** You create an instance of `FastAPI()` to define your API and register routes (`@app.get`, `@app.post`, etc.).
- **Without it:** You wouldn’t be able to start or run a FastAPI app.

### 2. `from pydantic import BaseModel, Field`

- **Purpose:** Pydantic is used for **data validation and serialization**.
  - `BaseModel`: Lets you define request/response schemas (e.g., your `Book` model).
  - `Field`: Allows you to add constraints (like `min_length`, `max_length`, `gt`, `lt`) and metadata to model attributes.
- **Usage:** Ensures incoming JSON data matches your schema and automatically validates it.
- **Without it:** You’d have to manually validate request data, which is error-prone and repetitive.

### 3. `from uuid import UUID`

- **Purpose:** Provides a standard way to represent unique identifiers.
- **Usage:** In your `Book` model, `id: UUID` ensures each book has a globally unique ID.
- **Without it:** You’d likely fall back to plain strings or integers, which are less reliable for uniqueness across distributed systems.

### Quick Example in Context

```python
class Book(BaseModel):
    id: UUID                                # Unique identifier
    title: str = Field(min_length=1)        # Title must be at least 1 character
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)      # Rating between 0–100
```

Here:

- `FastAPI` runs the app.
- `BaseModel` defines the schema.
- `Field` enforces validation rules.
- `UUID` ensures unique IDs.

---

### Updated Code with Auto-Generated UUIDs

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID, uuid4   # Import uuid4 to auto-generate UUIDs

# Create FastAPI app instance
app = FastAPI()

# ============================
# Define Book model (without requiring id from client)
# ============================
class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)   # Auto-generate UUID if not provided
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

# ============================
# In-memory storage
# ============================
BOOKS = []

# ============================
# Routes
# ============================

@app.get("/")
def read_api():
    """Root endpoint: returns a welcome message"""
    return {"Welcome": "Tareq"}

@app.post("/book")
def create_book(book: Book):
    """Creates a new book with auto-generated UUID"""
    BOOKS.append(book)
    return book

@app.get("/book")
def get_books():
    """Returns all stored books"""
    return BOOKS
```

### Key Change

- `id: UUID = Field(default_factory=uuid4)`  
  This means:
  - If the client **doesn’t send an `id`**, FastAPI will automatically generate one using `uuid4()`.
  - If the client **does send an `id`**, it will use that instead.

---

### Example Request (no `id` provided)

```json
POST /book
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "description": "A handbook of agile software craftsmanship",
  "rating": 95
}
```

### Example Response (UUID auto-generated)

```json
{
  "id": "c1a9f3d2-7f8b-4a6c-9d3e-2f5a7c8b9e1f",
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "description": "A handbook of agile software craftsmanship",
  "rating": 95
}
```

---

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

---

### 🔹 Step 2: Access Endpoints in Browser

Here’s how you can test each route:

| Endpoint                 | URL to Visit                                                                                                                                 | What You’ll See                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Root (`/`)               | [http://127.0.0.1:8000/](http://127.0.0.1:8000/)                                                                                             | `{"Welcome": "Tareq"}`                                  |
| About (`/about`)         | `http://127.0.0.1:8000/about` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fabout")                   | `{"About": "This is a demo FastAPI project by Tareq."}` |
| Hello (`/hello/{name}`)  | `http://127.0.0.1:8000/hello/Tareq` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fhello%2FTareq")     | `{"Message": "Hello, Tareq! Welcome to FastAPI."}`      |
| Square (`/square?num=5`) | `http://127.0.0.1:8000/square?num=5` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fsquare%3Fnum%3D5") | `{"Number": 5, "Square": 25}`                           |

---

### 🔹 Step 3: Use Interactive Docs

FastAPI automatically generates API documentation:

- **Swagger UI** → `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")  
  → Interactive interface where you can test endpoints directly.

- **ReDoc** → `http://127.0.0.1:8000/redoc` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fredoc")  
  → Clean, read-only documentation.

---

### 🔹 Step 4: Test with `curl` (optional)

If you prefer command line testing:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/about
curl http://127.0.0.1:8000/hello/Tareq
curl "http://127.0.0.1:8000/square?num=7"
```

---

### 🔹 Step 5: Test with Postman (optional)

- Open Postman.
- Create a new request.
- Set method to **GET**.
- Enter the endpoint URL (e.g., `http://127.0.0.1:8000/hello/Tareq`).
- Click **Send** → You’ll see the JSON response.

---

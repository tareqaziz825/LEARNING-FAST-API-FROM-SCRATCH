from fastapi import FastAPI

app = FastAPI()

def greet():
    return "Welcome to my Project!"


greet()

# (fastapienv) PS E:\LEARNING-FAST-API-FROM-SCRATCH\telusko> uvicorn main:app --reload

# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
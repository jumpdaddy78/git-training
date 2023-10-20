from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello"}

@app.get("/todos")
def get_todos():
    return "get todo"


from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from schemas import LoginRequest, TaskRequest
from auth import authenticate_user
from models import create_task

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_login():
    return FileResponse("static/login.html")

@app.post("/login")
def login(request: LoginRequest):
    user = authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "email": user["email"]
        }
    }

@app.get("/create-task-form")
def serve_create_task():
    return FileResponse("static/create-task.html")



@app.post("/create-task")
def create_task_endpoint(request: TaskRequest):
    task_id = create_task(request.name, request.date.isoformat(), request.task_details)
    return {
        "message": "Task created successfully",
        "task_id": task_id
    }

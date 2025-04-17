from pydantic import BaseModel, EmailStr
from datetime import date

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TaskRequest(BaseModel):
    name: str
    date: date
    task_details: str

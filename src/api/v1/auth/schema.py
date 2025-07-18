from pydantic import BaseModel, EmailStr, constr, Field, constr
from typing import Optional
from enum import Enum
from datetime import datetime


# Enum for user roles
class UserRole(str, Enum):
    admin = "admin"
    user = "user"

# Base user info for display

class User(BaseModel):
    unique_id: str
    first_name: str
    last_name: str
    email: EmailStr
    role: UserRole
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# Schema for login
class UserLogin(BaseModel):
    user_id: str
    password: constr(min_length=6)

# Schema for basic user registration
class AddUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    state: str
    country: Optional[str] = "India"
    phone: str
    language: str
    password: str
    grade: str
    role: Optional[str] = "user"


# Schema for full user creation (e.g. by admin)
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    state: str
    country: Optional[str] = Field(default="India")
    phone: str
    language: str
    email: EmailStr
    password: constr(min_length=6)
    grade: str
    role: Optional[UserRole] = Field(default=UserRole.user)

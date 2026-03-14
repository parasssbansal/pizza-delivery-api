from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional
class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str
    phone:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:str
    class Config:
        from_attributes=True


class LoginSchema(BaseModel):
    email:EmailStr
    password:str

class PasswordUpdate(BaseModel):
    password:str
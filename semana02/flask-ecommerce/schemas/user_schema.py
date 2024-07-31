from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    rol_id: int

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class UpdateUserSchema(UserSchema):
    status: bool
    password: Optional[str] = None
    password_confirm: Optional[str] = None 

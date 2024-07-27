from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    rol_id: int

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
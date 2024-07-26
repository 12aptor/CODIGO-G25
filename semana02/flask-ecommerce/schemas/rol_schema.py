from pydantic import BaseModel

class RolSchema(BaseModel):
    name: str

class UpdateRolSchema(BaseModel):
    name: str
    status: bool
from pydantic import BaseModel

class RolSchema(BaseModel):
    name: str

class UpdateRolSchema(RolSchema):
    status: bool
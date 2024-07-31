from pydantic import BaseModel

class CategorySchema(BaseModel):
    name: str

class UpdateCategorySchema(CategorySchema):
    status: bool
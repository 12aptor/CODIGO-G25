from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    code: str
    description: str
    brand: str
    size: str
    price: float
    stock: int
    category_id: int
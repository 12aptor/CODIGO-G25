from pydantic import BaseModel, Field

class OrderDetailSchema(BaseModel):
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    subtotal: float = Field(gt=0)
    product_id: int

class OrderSchema(BaseModel):
    client_name: str
    client_last_name: str
    client_address: str
    client_document_number: str
    total: float = Field(gt=0)
    order_details: list[OrderDetailSchema]
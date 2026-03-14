from pydantic import BaseModel
class OrderItems(BaseModel):
    pizza_id:int
    quantity:int
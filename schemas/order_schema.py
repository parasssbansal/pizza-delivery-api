from pydantic import BaseModel
from typing import List
from schemas.order_item_schema import OrderItems
from datetime import datetime
class OrderCreate(BaseModel):
    items:List[OrderItems]
    address_id:int

class OrderResponse(BaseModel):
    id:int
    user_id:int
    total_price:float
    status:str
    created_at:datetime
    class Config:
        from_attributes=True


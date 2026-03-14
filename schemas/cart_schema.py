from pydantic import BaseModel
class CartCreate(BaseModel):
    pizza_id:int
    quantity:int
class CartResponse(BaseModel):
    id:int
    user_id:int
    pizza_id:int
    quantity:int

    class Config:
        from_attributes=True
from pydantic import BaseModel
class AddressCreate(BaseModel):
    street:str
    city:str
    pin_code:int

class AddressResponse(BaseModel):
    id:int
    user_id:int
    street:str
    city:str
    pin_code:int
    class Config:
        from_attributes=True
from pydantic import BaseModel
class PizzaCreate(BaseModel):
    id:int
    name:str
    description:str
    price:float
    size:str
    category:str
    available:int

class PizzaUpdate(BaseModel):
    name:str
    description:str
    price:float
    size:str
    category:str
    available:int

class PizzaResponse(BaseModel):
    id:int
    name:str
    description:str
    price:float
    size:str
    category:str
    available:int

    class Config:
        from_attributes=True
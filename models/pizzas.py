from sqlalchemy import Column, Integer, String
from database import Base
class Pizzas(Base):
    __tablename__='pizzas'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Integer)
    size=Column(String)
    category=Column(String)
    available=Column(Integer)
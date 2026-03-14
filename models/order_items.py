from sqlalchemy import Column, Integer, String
from database import Base
class OrderItems(Base):
    __tablename__='order_items'
    id=Column(Integer, primary_key=True, index=True)
    order_id=Column(Integer)
    pizza_id=Column(Integer)
    quantity=Column(Integer)
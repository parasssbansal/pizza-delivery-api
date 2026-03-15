from sqlalchemy import Integer, String, Column , DateTime , Float
from sqlalchemy.sql import func
from database import Base
class Orders(Base):
    __tablename__='orders'
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer)
    total_price=Column(Float,default=0)
    status=Column(String,default="Order Placed")
    created_at=Column(DateTime,server_default=func.now())
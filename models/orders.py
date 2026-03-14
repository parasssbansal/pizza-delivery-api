from sqlalchemy import Integer, String, Column , DateTime
from sqlalchemy.sql import func
from database import Base
class Orders(Base):
    __tablename__='orders'
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer)
    total_price=Column(Integer)
    status=Column(String)
    created_at=Column(DateTime,server_default=func.now())
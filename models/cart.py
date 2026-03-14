from sqlalchemy import Column,Integer,String, UniqueConstraint
from database import Base
class Cart(Base):
    __tablename__='cart'
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    pizza_id=Column(Integer)
    quantity=Column(Integer)
    __table_args__ = (
        UniqueConstraint('user_id', 'pizza_id', name='unique_user_pizza'),
    )
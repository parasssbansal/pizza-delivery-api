from sqlalchemy import Column, Integer, String
from database import Base
class Adress(Base):
    __tablename__='address'
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer)
    street=Column(String)
    city=Column(String)
    pin_code=Column(String)
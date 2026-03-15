from fastapi import APIRouter , HTTPException , Depends
from sqlalchemy.orm import Session
from database import get_db
from models.orders import Orders
from schemas.order_schema import OrderCreate , OrderResponse
from utils.jwt import get_current_user
from models.cart import Cart
from models.users import User
from models.pizzas import Pizzas
from typing import List

router=APIRouter(prefix="/orders",tags=["Orders"])

@router.post("/place_order")
def create_order(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id=current_user.id
    cart_items=db.query(Cart).filter(Cart.user_id==user_id).all()
    if not cart_items:
        raise HTTPException(status_code=404,detail="Cart is Empty")
    total_price=0
    for item in cart_items:
        pizza=db.query(Pizzas).filter(Pizzas.id==item.pizza_id).first()
        total_price+=pizza.price*item.quantity
    new_order=Orders(
        user_id=user_id,   
        total_price=total_price,
        status="Order Placed"
    )
    cart=db.query(Cart).filter(Cart.user_id==user_id).delete()
    db.add(new_order)
    db.commit()
    db.refresh(new_order)


    return new_order

@router.get("/view",response_model=List[OrderResponse])
def get_order(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id=current_user.id
    db_order=db.query(Orders).filter(Orders.user_id==user_id).all()
    if not db_order:
        raise HTTPException(status_code=404,detail="No orders yet..")
    return db_order

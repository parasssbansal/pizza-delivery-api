from fastapi import APIRouter, HTTPException , Depends
from sqlalchemy.orm import Session
from database import get_db
from models.cart import Cart
from schemas.cart_schema import CartCreate, CartResponse 
from utils.jwt import get_current_user
from models.pizzas import Pizzas
router=APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/add", response_model=CartResponse)
def add_to_cart(
    cart: CartCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    if cart.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")

    db_pizza = db.query(Pizzas).filter(Pizzas.id == cart.pizza_id).first()
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza Not Found")

    cart_item = db.query(Cart).filter(
        Cart.user_id == user_id,
        Cart.pizza_id == cart.pizza_id
    ).first()

    if cart_item:
        cart_item.quantity += cart.quantity
    else:
        cart_item = Cart(
            user_id=user_id,
            pizza_id=cart.pizza_id,
            quantity=cart.quantity
        )
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)

    return cart_item

@router.get("/view",response_model=list[CartResponse])
def view_cart(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    carts = db.query(Cart).filter(Cart.user_id == user_id).all()
    return carts

@router.patch("/update/{cart_id}", response_model=CartResponse)
def update_cart(
    cart_id:int,
    quantity:int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_cart=db.query(Cart).filter(Cart.id==cart_id).first()
    if not db_cart:
        raise HTTPException(status_code=404, detail="Cart item not found")
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")
    db_cart.quantity=quantity
    db.commit()
    db.refresh(db_cart)
    return db_cart

@router.delete("/cart/remove/{pizza_id}")
def delete_cart_item(pizza_id:int, 
                     db:Session=Depends(get_db),
                     user_id:int=Depends(get_current_user)
                     ):
    db_cart=db.query(Cart).filter(Cart.pizza_id==pizza_id,Cart.user_id==user_id).first()
    if not db_cart:
        raise HTTPException(status_code=404,detail="Item not Found..")
    db.delete(db_cart)
    db.commit()
    return {"message":"Item sucessfully deleted"}

@router.delete("/delete")
def delete_cart(user_id:int=Depends(get_current_user),
                db:Session=Depends(get_db)
                ):
    
    cart_db=db.query(Cart).filter(Cart.user_id==user_id).delete()
    db.commit()
    return {"Message":"Cart sucessfully deleted"}

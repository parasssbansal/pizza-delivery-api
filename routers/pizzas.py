from fastapi import APIRouter, HTTPException , Depends
from sqlalchemy.orm import Session 
from database import get_db
from models.pizzas import Pizzas
from schemas.pizza_schema import PizzaCreate, PizzaResponse , PizzaUpdate

router=APIRouter()

@router.post("/add_pizza",response_model=PizzaResponse)
def add_pizza(pizza:PizzaCreate,db:Session=Depends(get_db)):
    new_pizza=Pizzas(
        id=pizza.id,
        name=pizza.name,
        description=pizza.description,
        price=pizza.price,
        size=pizza.size,
        category=pizza.category,
        available=pizza.available
    )
    db.add(new_pizza)
    db.commit()
    db.refresh(new_pizza)
    return new_pizza

@router.get("/get_pizzas",response_model=list[PizzaResponse])
def get_pizzas(db:Session=Depends(get_db)):
    pizzas=db.query(Pizzas).all()
    return pizzas

@router.get("/get_pizza/{pizza_id}",response_model=PizzaResponse)
def get_pizza(pizza_id:int,db:Session=Depends(get_db)):
    pizza=db.query(Pizzas).filter(Pizzas.id==pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404,detail="Pizza Not Found")
    return pizza

@router.put("/update_pizza/{pizza_id}",response_model=PizzaResponse)
def update_pizza(pizza_id:int,pizza:PizzaUpdate,db:Session=Depends(get_db)):
    db_pizza=db.query(Pizzas).filter(Pizzas.id==pizza_id).first()
    if not db_pizza:
        raise HTTPException(status_code=404,detail="Pizza Not Found")
    db_pizza.name=pizza.name
    db_pizza.description=pizza.description
    db_pizza.price=pizza.price
    db_pizza.size=pizza.size
    db_pizza.category=pizza.category
    db_pizza.available=pizza.available
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

@router.delete("/delete_pizza/{pizza_id}")
def delete_pizza(pizza_id:int,db:Session=Depends(get_db)):
    db_pizza=db.query(Pizzas).filter(Pizzas.id==pizza_id).first()
    if not db_pizza:
        raise HTTPException(status_code=404,detail="Pizza Not Found")
    db.delete(db_pizza)
    db.commit()
    return {"message":"Pizza Deleted Successfully"}
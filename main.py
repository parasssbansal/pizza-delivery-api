from fastapi import FastAPI
from database import Base, engine

# import models first
from models import users, address, cart, orders, order_items

# import routers
from routers import auth, cart, orders, pizzas, users

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(pizzas.router)
app.include_router(cart.router)
app.include_router(orders.router)
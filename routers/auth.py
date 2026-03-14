from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from schemas.user_schema import UserCreate, UserResponse , LoginSchema
from utils.hashing import hash_password, verify_password
from utils.jwt import create_access_token
from pydantic import EmailStr
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password=hash_password(user.password)
    new_user=User(name=user.name,email=user.email,password=hashed_password,phone=user.phone)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), 
          db:Session=Depends(get_db)
          ):
    db_user=db.query(User).filter(User.email==form_data.username).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    if not verify_password(form_data.password,db_user.password):
        return {"Error":"Invalid Password"}
    token = create_access_token(
        data={"sub": str(db_user.id)}
        )
    return {
        "access_token": token,
        "token_type": "bearer"
    }

  
from fastapi import APIRouter , Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.users import User
from schemas.user_schema import UserCreate, UserResponse , LoginSchema , PasswordUpdate
from typing import List
from utils.hashing import hash_password, verify_password
router=APIRouter()
from pydantic import EmailStr

@router.get("/allusers",response_model=List[UserResponse])
def get_allusers(db:Session=Depends(get_db)):
    users=db.query(User).all()
    return users

@router.get("/view_profile/{user_id}",response_model=UserResponse)
def view_profile(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    return user

@router.put("/update_profile/{user_id}",response_model=UserResponse)
def update_profile(user_id:int, user:UserCreate,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    db_user.name=user.name
    db_user.email=user.email
    db_user.phone=user.phone
    db.commit()
    db.refresh(db_user)
    return db_user

@router.patch("/update_password/{email_id}")
def update_password(email_id:EmailStr,data:PasswordUpdate,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==email_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    if verify_password(data.password,db_user.password):
        raise HTTPException(status_code=400,detail="New password cannot be the same as the old password")
    hashed_password=hash_password(data.password)
    db_user.password=hashed_password
    db.commit()
    db.refresh(db_user)
    return {"message":"Password Updated Successfully"}
    

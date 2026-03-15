from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from db import DBsession
from models import User

router = APIRouter(prefix="/user", tags=['Users'])

@router.get("/")
def get_all_users(db: DBsession):
    db_users = db.exec(select(User)).all()
    return db_users

@router.get("/getuserbyid/{user_id}")
def get_userbyid(user_id: int, db: DBsession):
    db_user = db.exec(select(User).where(User.id==user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} Not Found"
        )
    return db_user

@router.post("/adduser")
def add_user(user: User, db: DBsession):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/updateuser/{user_id}")
def update_user(user_id: int, db: DBsession, user: User):
    db_user = db.exec(select(User).where(User.id==user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} Not Found"
        )
    
    db_user.id = user.id
    db_user.name = user.name
    db_user.user_name = user.user_name
    db_user.age = user.age


    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/deleteuser/{user_id}")
def delete_user(user_id: int, db: DBsession):
    db_user = db.exec(select(User).where(User.id==user_id)).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} Not found"
        )
    db.delete(db_user)
    db.commit()
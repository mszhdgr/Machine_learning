from fastapi import APIRouter, HTTPException, status
from db import DBsession
import models
from schemas import UserCreate


router = APIRouter(prefix="/user", tags=['Users Crud'])

@router.get("/")
def get_all_users(db: DBsession):
    users = db.query(models.User).all()
    return users

@router.get("/{user_id}")
def get_user_byId(user_id: int, db: DBsession):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with Id: {user_id} Not found"
        )
    return db_user


@router.post("/adduser")
def add_user(db: DBsession, user: UserCreate):
    db_user = models.User(id=user.id, name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/updateuser/{user_id}")
def update_user(user_id: int, db: DBsession, user: UserCreate):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with Id: {user_id} Not found"
        )
    if db_user:
        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email = user.email
        
        db.commit()
        db.refresh(db_user)
    return db_user

@router.delete("/deleteuser/{user_id}")
def delete_user(user_id: int, db: DBsession):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with Id: {user_id} Not found"
        )
    
    db.delete(db_user)
    db.commit()
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail=f"USER WITH ID: {user_id} DELETED SUCCESSFULLY"
    )
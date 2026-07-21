from fastapi import APIRouter, HTTPException, status
from schemas import Get_item, Create_item
from auth import DB_SESSION
from models import Items
from sqlmodel import select
from typing import List


router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=List[Get_item])
def get_items(db: DB_SESSION):
    db_items = db.exec(select(Items)).all()
    return db_items

@router.post("/", response_model=Get_item)
def create_item(db: DB_SESSION, data: Create_item):
    db_items = Items(
        name=data.name,
        quantity=data.quantity
    )
    db.add(db_items)
    db.commit()
    db.refresh(db_items)
    return db_items

@router.put("/", response_model=Get_item)
def update_item(id: int, db: DB_SESSION, new_item: Create_item):
    db_user = db.exec(select(Items).filter(Items.id==id)).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Item with id: {id} NOT FOUND"
            )
    
    update_data = new_item.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/")
def delete_item(id: int, db: DB_SESSION):
    db_user = db.exec(select(Items).filter(Items.id==id)).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id: {id} NOT FOUND"
            )
    db.delete(db_user)
    db.commit()
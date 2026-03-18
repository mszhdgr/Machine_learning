from fastapi import APIRouter, HTTPException, status, Request
from db import DB_Session
from models import Books
from sqlmodel import select
from limiter_config import limiter


router = APIRouter(prefix="/books", tags=['Books'])

@router.get("/",
            status_code=status.HTTP_200_OK
            )
@limiter.limit("2/minute")
async def get_all_books(db: DB_Session, request: Request):
    all_books = db.exec(select(Books)).all()
    return all_books

@router.get("/getbook/{book_id}",
            status_code=status.HTTP_200_OK
            )
@limiter.limit("2/minute")
async def get_a_single_book(book_id: int, db: DB_Session, request: Request):
    db_book = db.exec(select(Books).where(Books.id==book_id)).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with Id: {book_id} NOT FOUND"
        )
    return db_book

@router.post("/addbook",
             status_code=status.HTTP_201_CREATED,
             response_description="Book created successfully"
            )
@limiter.limit("2/minute")
async def add_a_book(new_book: Books, db: DB_Session, request: Request):
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/updatebook/{book_id}",
            status_code=status.HTTP_205_RESET_CONTENT,
            response_description="book updated"
            )
@limiter.limit("2/minute")
async def update_a_book(book_id: int, new_book: Books, db: DB_Session, request: Request):
    db_book = db.exec(select(Books).where(Books.id==book_id)).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id: {book_id} Not Found"
        )
    
    new_book_data = new_book.model_dump(exclude_unset=True)

    for key, value in new_book_data.items():
        setattr(db_book, key, value)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/deletebook/{book_id}",
               status_code=status.HTTP_202_ACCEPTED,
               response_description="Deleted Succesfully"
               )
@limiter.limit("2/minute")
async def delete_a_book(book_id: int, db:DB_Session,request: Request):
    db_book = db.exec(select(Books).where(Books.id==book_id)).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id: {book_id} Not Found"
        )
    db.delete(db_book)
    db.commit()
from fastapi import APIRouter, HTTPException, status
from schemas import BooksGetRes, AddBook
from typing import List


router = APIRouter(prefix="/books", tags=["Books"])

books_db = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 4, "title": "Project Hail Mary", "author": "Andy Weir"},
    {"id": 5, "title": "Dune", "author": "Frank Herbert"},
    {"id": 6, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 7, "title": "Foundation", "author": "Isaac Asimov"},
    {"id": 8, "title": "The Silent Patient", "author": "Alex Michaelides"},
    {"id": 9, "title": "Neuromancer", "author": "William Gibson"},
    {"id": 10, "title": "The Alchemist", "author": "Paulo Coelho"}
]

@router.get("/", response_model=List[BooksGetRes])
def all_books():
    return books_db

@router.get("/singlebook", response_model=List[BooksGetRes])
def get_abook(book_id: int):

    Book = [book for book in books_db if book["id"] == book_id]

    if not Book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {book_id} Not Found")
    
    return Book

@router.post("/addbook")
def add_book(user_input: AddBook):
    books_db.append(user_input)
    return user_input

@router.put("/updatebook")
def update_book(id: int, newbook: AddBook):
    
    for index, book in enumerate(books_db):
        if book["id"] == id:
            updated_data = newbook.model_dump()
            updated_data["id"] = id

            book[index] = updated_data
            return HTTPException(status_code=status.HTTP_200_OK, detail="Updated Successfully")
        
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Post created")

@router.delete("/deletebook")
def delete_book(id: int):

    for index, book in enumerate(books_db):
        if book["id"] == id:
            deleted_book = books_db.pop(index)
            return {"Message":f"Book: {deleted_book} was removed"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {id} Not Found")
    


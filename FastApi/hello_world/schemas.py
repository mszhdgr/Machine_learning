from pydantic import BaseModel

class BooksGetRes(BaseModel):
    title: str
    author: str

class AddBook(BooksGetRes):
    id: int

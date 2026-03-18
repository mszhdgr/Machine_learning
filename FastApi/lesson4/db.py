from sqlmodel import create_engine, Session, SQLModel
from typing import Annotated
from fastapi import Depends

DATABASE_URL = "sqlite:///library.db"

connect_args = {"check_same_thread" : False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

def create_database_and_tables():
    return SQLModel.metadata.create_all(bind=engine)

def create_session():
    with Session(engine) as session:
        yield session


DB_Session = Annotated[Session, Depends(create_session)]
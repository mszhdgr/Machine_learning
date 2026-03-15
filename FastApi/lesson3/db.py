from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends

DATABASE_URL = "sqlite:///users.db"

connect_args = {"check_same_thread" : False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

DBsession = Annotated[Session, Depends(get_session)]
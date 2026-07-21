from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
from fastapi import Depends
from typing import Annotated
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
connect_args = {"check_same_thread": False}

engine = create_engine(url=DB_URL, connect_args=connect_args)

def create_database_and_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session


DB_SESSION = Annotated[Session, Depends(get_session)]
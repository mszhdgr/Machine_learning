from sqlmodel import SQLModel
from typing import Optional

class Get_item(SQLModel):
    name: str
    quantity: int

class Create_item(Get_item):
    pass
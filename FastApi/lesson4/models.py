from sqlmodel import SQLModel, Field

class Books(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None, index=True)
    author: str
    published: bool = Field(default=True)
from fastapi import FastAPI
from db import create_db_and_tables
from contextlib import asynccontextmanager
from routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

    print("Shutting Down Application")

app = FastAPI(lifespan=lifespan)


@app.get("/",tags=['Home'])
def home():
    return {"Message":"Welcome Home people"}

app.include_router(router=router)
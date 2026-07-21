from fastapi import FastAPI
from contextlib import asynccontextmanager
from auth import create_database_and_tables
from routes import router as item_routes

@asynccontextmanager
async def lifespan(FastAPI):
    create_database_and_tables()
    yield
    print("Shutting Down")

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Home"])
def home():
    return {"home":"welcome home baby"}

app.include_router(router=item_routes)
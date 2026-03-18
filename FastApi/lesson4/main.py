
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from db import create_database_and_tables
from routes import router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter_config import limiter


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database_and_tables()
    yield
    print("Program shutting down")


app = FastAPI(lifespan=lifespan)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/", tags=['Home'])
@limiter.limit("5/minute")
async def home(request: Request):
    return {"Message": "Welcome Home"}

app.include_router(router=router)
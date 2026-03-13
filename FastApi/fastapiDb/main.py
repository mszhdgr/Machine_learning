from fastapi import FastAPI
import models
from db import engine
from routers import router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"Message": "Welcome Home"}

app.include_router(router)
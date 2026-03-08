from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/", tags=["Home"])
def root():
    return {"Message" : "Welcome To My Bookshop"}

app.include_router(router=router)
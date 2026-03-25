from fastapi import FastAPI
from mlflow.sklearn import load_model
import numpy as np
from .schemas import UserInput

app = FastAPI()

model = load_model(f"runs:/9c0d7e81e8244843b2ea5997db2f2312/model")

@app.get("/")
def home():
    return {"message":"Welcome Home"}


@app.post("/preds")
def get_prediction(features: UserInput):
    
    data = features.model_dump()
    array = []

    for _, value in data.items():
        array.append(value)

    x = np.array(array).reshape(1, -1)

    prediction = model.predict(x)
    pred = prediction.tolist()
    class_to_idx = {0:"setosa",1:"versicolor",2:"virginica"}

    return {"Predicted Class": class_to_idx[pred[0]]}
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="E-Commerce Purchase Prediction API")

model = joblib.load("models/gradient_boosting_model.pkl")
scaler = joblib.load("models/scaler.pkl")


class CustomerData(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {
        "message": "E-Commerce Purchase Prediction API is running!"
    }


@app.post("/predict")
def predict(data: CustomerData):

    features = np.array(data.features).reshape(1, -1)

    features = scaler.transform(features)

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }
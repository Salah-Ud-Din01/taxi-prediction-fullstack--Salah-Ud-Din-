# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the saved best model
model = joblib.load("models/taxi_model.joblib")  # make sure this path is correct

#  Initialize FastAPI
app = FastAPI(title="Taxi Trip Price Prediction API")

#  Define input schema (matches numeric features in your model)
class TripInput(BaseModel):
    Trip_Distance_km: float
    Passenger_Count: int

# Test endpoint
@app.get("/")
def root():
    return { "Taxi Trip Price Prediction API is running"}

#  Prediction endpoint
@app.post("/predict")
def predict(trip: TripInput):
    # Convert input to dataframe
    features = pd.DataFrame([trip.dict()])

    # Predict using trained model
    price = model.predict(features)[0]

    return {"predicted_price": round(float(price), 2)}

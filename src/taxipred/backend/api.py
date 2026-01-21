from fastapi import FastAPI
from pydantic import BaseModel

# Minimal dummy backend — guaranteed to run
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Taxi Prediction API is running"}

class TripInput(BaseModel):
    trip_distance: float
    passenger_count: int
    pickup_hour: int

@app.post("/predict")
def predict(trip: TripInput):
    # Dummy predictable price just to test
    price = trip.trip_distance * 2 + trip.passenger_count * 0.5
    return {"predicted_price": round(price, 2)}


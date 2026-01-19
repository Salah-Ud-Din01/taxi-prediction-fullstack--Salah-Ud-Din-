from fastapi import FastAPI
from pydantic import BaseModel
from backend.data_processing import load_data, predict_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Taxi Prediction API is running"}


@app.get("/data")
def get_data(n_rows: int = 100):
    return load_data(n_rows).to_dict(orient="records")


class TripInput(BaseModel):
    trip_distance: float
    passenger_count: int
    pickup_hour: int


@app.post("/predict")
def predict(trip: TripInput):
    price = predict_price(trip.dict())
    return {"predicted_price": round(price, 2)}

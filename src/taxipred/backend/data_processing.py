import pandas as pd
import joblib
from pathlib import Path

# Base project path
BASE_PATH = Path(__file__).resolve().parents[2]

# Paths
DATA_PATH = BASE_PATH / "data" / "taxi_trip_pricing.csv"
MODEL_PATH = BASE_PATH / "model_development" / "models" / "taxi_model.pkl"

# Load trained model once
model = joblib.load(MODEL_PATH)


def load_data(n_rows: int = 100):
    return pd.read_csv(DATA_PATH).head(n_rows)


def predict_price(features: dict) -> float:
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return float(prediction[0])

import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_PATH / "data" / "taxi_trip_pricing.csv"

def load_data(n_rows: int = 100):
    return pd.read_csv(DATA_PATH).head(n_rows)

from pathlib import Path

# Root of the package (…/src/taxipred)
PACKAGE_ROOT = Path(__file__).resolve().parents[1]

# Data folder
DATA_PATH = PACKAGE_ROOT / "data"

# Taxi CSV file
TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"

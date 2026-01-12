from taxipred.utils.constants import TAXI_CSV_PATH
import pandas as pd

print(TAXI_CSV_PATH)

df = pd.read_csv(TAXI_CSV_PATH)
print(df.head())

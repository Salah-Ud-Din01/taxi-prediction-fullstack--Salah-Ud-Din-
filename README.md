# Taxi Price Prediction – Fullstack Project

## Description
This project predicts taxi prices using a machine learning model.
The application consists of a FastAPI backend and a Streamlit frontend.
The backend serves predictions through an API and the frontend consumes this API.

---

## Project Structure
taxi-prediction-fullstack--Salah-Ud-Din-
├── src/
│   └── taxipred/
│       ├── backend/
│       │   ├── api.py
│       │   └── data_processing.py
│       ├── data/
│       │   └── taxi_trip_pricing.csv
│       ├── frontend/
│       │   └── app.py
│       ├── model_development/
│       │   ├── models/
│       │   ├── eda.ipynb
│       │   └── model_dev.ipynb
│       └── utils/
│           └── __init__.py
├── README.md
├── requirements.txt
└── .gitignore



---

## Machine Learning
- Performed EDA on taxi trip data
- Cleaned data and removed outliers
- Trained a regression model
- Exported the model using `joblib`

---

## Backend (FastAPI)
The backend exposes the following endpoints:

- `GET /` – API health check
- `GET /data` – Returns sample taxi data
- `POST /predict` – Returns predicted taxi price

Example request:
```json
{
  "trip_distance": 5.0,
  "passenger_count": 1,
  "pickup_hour": 12
}

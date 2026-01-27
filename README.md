# Taxi Price Prediction – Fullstack Project

## Description
A fullstack application that predicts taxi prices using a machine learning model.  
The project consists of a **FastAPI backend** and a **Streamlit frontend**.

---

## Project Structure

# Taxi Price Prediction – Fullstack Project

## Description
A fullstack application that predicts taxi prices using a machine learning model.  
The project consists of a **FastAPI backend** and a **Streamlit frontend**.

---
taxi-prediction-fullstack/
├── screenshots/              # Application screenshots
├── src/
│   └── taxipred/
│       ├── backend/          # FastAPI backend
│       ├── frontend/         # Streamlit frontend
│       ├── data/             # Dataset
│       └── model_development/# EDA & model training
├── README.md
└── Video Link        # Demo video file




Machine Learning
Performed exploratory data analysis (EDA)
Cleaned the dataset and removed outliers
Trained a regression model
Exported the trained model using joblib

Backend (FastAPI)
The backend exposes the following endpoints:
GET / – API health check
GET /data – Returns sample taxi data
POST /predict – Returns predicted taxi price
Example request
{
  "trip_distance": 5.0,
  "passenger_count": 1,
  "pickup_hour": 12
}


Frontend (Streamlit)
The Streamlit frontend allows the user to:
Enter trip distance
Enter passenger count
Enter pickup hour
Get a predicted taxi price from the backend API

How to Run the Project
# create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# install dependencies
pip install -r requirements.txt
# run backend
cd src/taxipred/backend
uvicorn taxipred.backend.api:app --reload
# run frontend
cd src/taxipred/frontend
streamlit run app.py
Backend runs at:
http://127.0.0.1:8000

Technologies Used

Python
Pandas
Scikit-learn
FastAPI
Streamlit
Joblib
Git & GitHub
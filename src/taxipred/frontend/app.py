import streamlit as st
import requests

st.title("Taxi Price Prediction")

# Input fields
trip_distance = st.number_input("Trip Distance (km)", min_value=0.0, value=5.0)
passenger_count = st.number_input("Passenger Count", min_value=1, value=1)
pickup_hour = st.number_input("Pickup Hour (0-23)", min_value=0, max_value=23, value=12)

# Single button with unique key
if st.button("Predict Price", key="predict_button"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "trip_distance": trip_distance,
                "passenger_count": passenger_count,
                "pickup_hour": pickup_hour
            }
        )
        data = response.json()
        st.success(f"Predicted Price: ${data['predicted_price']}")
    except Exception as e:
        st.error(f"Backend response failed. Is the API running?\nError: {e}")

import streamlit as st
import requests

st.title("Taxi Trip Price Prediction")

st.subheader("Step 1: Enter Trip Details")
trip_distance = float(st.number_input("Trip Distance (km)", min_value=0.0, value=5.0))
passenger_count = int(st.number_input("Passenger Count", min_value=1, value=1))
pickup_hour = int(st.number_input("Pickup Hour (0-23)", min_value=0, max_value=23, value=12))

# Optional: map hour to time of day
def map_hour_to_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

st.markdown("---") 
st.subheader("Step 2: Predict Price")  

if st.button("Predict Price"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "Trip_Distance_km": trip_distance,
                "Passenger_Count": passenger_count,
                "Base_Fare": 2.5,            # default value
                "Per_Km_Rate": 1.5,          # default value
                "Per_Minute_Rate": 0.2,      # default value
                "Trip_Duration_Minutes": 15, # default value
                "Time_of_Day": map_hour_to_time_of_day(pickup_hour),
                "Day_of_Week": "Monday",     # default value
                "Traffic_Conditions": "Light",
                "Weather": "Clear"
            }
        )

        data = response.json()
        st.success(f"Predicted Price: ${data['predicted_price']}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed. Check backend.\n{e}\nResponse text: {getattr(e.response, 'text', '')}")

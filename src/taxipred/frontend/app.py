import streamlit as st
import requests

st.title("Price prediction fro taxi trips")


st.subheader("Step 1: Enter Trip Details")
trip_distance = float(st.number_input("Trip Distance (km)", min_value=0.0, value=5.0))
passenger_count = int(st.number_input("Passenger Count", min_value=1, value=1))
pickup_hour = int(st.number_input("Pickup Hour (0-23)", min_value=0, max_value=23, value=12))

st.markdown("---") 
st.subheader("Step 2: Predict Price")  
if st.button("Predict Price", key="predict_button"):
    try:
        
        response = requests.post(
    "http://127.0.0.1:9000/predict",  
            json={
                "trip_distance": trip_distance,  
                "passenger_count": passenger_count,
                "pickup_hour": pickup_hour
            }
        )

      
        data = response.json()
        st.success(f"Predicted Price: ${data['predicted_price']}")
    except requests.exceptions.RequestException as e:
            st.error(f"Request failed. Check backend.\n{e}\nResponse text: {getattr(e.response, 'text', '')}")




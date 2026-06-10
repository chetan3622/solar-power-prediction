import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("solar_power_model.pkl")

st.title("Solar Power Generation Prediction")

st.write("Enter Weather Details")

distance_to_solar_noon = st.number_input("Distance to Solar Noon")
temperature = st.number_input("Temperature")
wind_direction = st.number_input("Wind Direction")
wind_speed = st.number_input("Wind Speed")
sky_cover = st.number_input("Sky Cover")
visibility = st.number_input("Visibility")
humidity = st.number_input("Humidity")
avg_wind_speed = st.number_input("Average Wind Speed (Period)")
avg_pressure = st.number_input("Average Pressure (Period)")

if st.button("Predict Power Generation"):

    features = np.array([[
        distance_to_solar_noon,
        temperature,
        wind_direction,
        wind_speed,
        sky_cover,
        visibility,
        humidity,
        avg_wind_speed,
        avg_pressure
    ]])

    prediction = model.predict(features)

    st.success(f"Predicted Power Generation: {prediction[0]:.2f}")
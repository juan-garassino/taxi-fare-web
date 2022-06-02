
import streamlit as st

import requests

import datetime

# retrieve prediction parameters

"# Manhattan ride parameters"

"Select a date and time"

date = st.date_input("Select a pickup date", datetime.date(2012, 10, 6))

time = st.time_input("Select a pickup time", datetime.time(8, 45))

pickup_datetime = f"{date} {time} UTC"  # "2012-10-06%2012:10:20%20UTC"

"Select a pickup location"

pickup_longitude = st.number_input("Pickup longitude", value=40.7614327)
pickup_latitude = st.number_input("Pickup latitude", value=-73.9798156)

"Select a dropoff location"

dropoff_longitude = st.number_input("Dropoff longitude", value=40.6513111)
dropoff_latitude = st.number_input("Dropoff latitude", value=-73.8803331)

"Select a passenger count"

passenger_count = st.slider("Passenger count", 1, 10, 3)

# request prediction from api

url = "https://taxifaremodelapi.herokuapp.com/predict_fare"
# url = "http://127.0.0.1:5000/predict_fare"

params = dict(
    key="2012-10-06%2012:10:20.0000001",  # this is unused by the model
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

response = requests.get(url, params=params).json()

prediction = response['prediction']

# display response to user

f"Predicted ride cost: {prediction}"

# app.py
from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import os
import requests
from dataclasses import dataclass #yt

app = Flask(__name__)

# Use your OpenWeatherMap API key
api_key = os.getenv('API_KEY', '1e966323c33f0d2fc4f0998d97533e82')

def get_lan_lon(city_name, state_code, country_code, API_key):
    """Get latitude and longitude for a given city."""
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}'
    ).json()

    # Extract latitude and longitude
    coord = resp.get('coord', {})
    lat = coord.get('lat')
    lon = coord.get('lon')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    """Fetch current weather data using latitude and longitude."""
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
    ).json()

    # Extract specific data
    temperature = resp.get('main', {}).get('temp')  # Temperature in Celsius
    weather_main = resp.get('weather', [{}])[0].get('main')  # Weather condition
    weather_description = resp.get('weather', [{}])[0].get('description')  # Description
    wind_speed = resp.get('wind', {}).get('speed')  # Wind speed in m/s
    cloud_cover = resp.get('clouds', {}).get('all')  # Cloud cover percentage

    # Display data
    print("Current Weather Data:")
    print(f"Temperature: {temperature} °C")
    print(f"Condition: {weather_main}")
    print(f"Description: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Cloud Cover: {cloud_cover}%")


if __name__ == "__main__":
    # Correct function call with separate arguments
    lat, lon = get_lan_lon('Kuala Lumpur', 'KL', 'Malaysia', api_key)
    print(f"Latitude: {lat}, Longitude: {lon}")

    # Get current weather using latitude and longitude
    get_current_weather(lat, lon, api_key)

# Load your trained model
with open("model/predictive_model.sav", "rb") as model_file:
    model = pickle.load(model_file)

# Define the home route
@app.route('/')
def home():
    return render_template('')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()  # Get data from form
    # Convert data to DataFrame to feed to model
    df = pd.DataFrame([data])  # Adjust this to match model input format

    # Make prediction
    prediction = model.predict(df)

    # Return result as JSON
    return jsonify({'prediction': prediction[0]})


# @app.route("/monthly.html")
# def weather_calendar():
#     # Generate the calendar
#     generate_calendar()  
#     return send_file("calendar.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)



'''from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/predictive_model.sav')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        data = [float(request.form['temp']), float(request.form['humidity']), ...]  # add relevant features
        prediction = model.predict([data])

        return render_template('index.html', prediction_text=f'Predicted Weather Condition: {prediction[0]}')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)'''

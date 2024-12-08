# app.py
from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

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

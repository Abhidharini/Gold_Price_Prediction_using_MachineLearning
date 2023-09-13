# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q4VZ0zgudQvgbONx9wBATEvAkNRh7BEY
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = StandardScaler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        input_data = [float(x) for x in request.form.values()]

        # Standardize the input data
        input_data = scaler.transform([input_data])

        # Make a prediction
        predicted_price = model.predict(input_data)

        return render_template('index.html', prediction=f'Predicted Gold Price: {predicted_price[0]:.2f}')
    except Exception as e:
        return render_template('index.html', prediction='Error: Invalid input')

if __name__ == '__main__':
    app.run(debug=True)


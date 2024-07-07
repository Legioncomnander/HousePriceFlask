from flask import Flask, render_template, request
import pandas as pd
import pickle
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('xgb_model.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction="Welcome, Press HOME to Start It")

@app.route('/predict', methods=['POST'])
def predict():
    # Mendapatkan data dari formulir HTML
    location = request.form['location_selected']
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    floors = float(request.form['floors'])
    view = float(request.form['view'])
    condition = float(request.form['condition'])
    sqft_above = float(request.form['sqft_above'])
    sqft_basement = float(request.form['sqft_basement'])
    age_house = float(request.form['age_house'])
    building_renewal = float(request.form['building_renewal'])
    
    # Membuat DataFrame dari input
    data = {
        'location': [location],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'floors': [floors],
        'view': [view],
        'condition': [condition],
        'sqft_above': [sqft_above],
        'sqft_basement': [sqft_basement],
        'age_house': [age_house],
        'building_renewal': [building_renewal]
    }
    input_df = pd.DataFrame(data)
    
    # Encoding untuk fitur kategorikal
    encode = ['location']  # Sesuaikan dengan nama kolom yang perlu di-encode
    input_encoded = pd.get_dummies(input_df, columns=encode)
    
    # Menambahkan kolom yang hilang dan mengatur ulang urutan kolom
    missing_cols = set(scaler.feature_names_in_) - set(input_encoded.columns)
    for col in missing_cols:
        input_encoded[col] = 0
    input_encoded = input_encoded[scaler.feature_names_in_]
    
    # Menggunakan scaler yang sama dengan training untuk transformasi data
    input_scaled = scaler.transform(input_encoded)
    
    # Melakukan prediksi dengan model
    prediction = model.predict(input_scaled)
    
    return render_template('index.html', prediction=f"${prediction[0]:,.2f}")

if __name__ == "__main__":
    app.run(debug=True)


import streamlit as st
import pandas as pd
import numpy as np
import joblib

#load the trained model
model_path = "food_price_model.pkl"
model = joblib.load(model_path)

#Define streamlit UI
st.title("Food Price Predicting App")
st.write("This app predicts future prices of farm produce (50KG bag or per tuber). While not 100% accurate, it helps you plan your budget with a rough estimate.")

#User input fields
Product = st.selectbox("Product", ['Cassava_meal', 'Cowpeas', 'Gari', 'Groundnuts', 'Maize', 'Millet', 'Rice', 'Sorghum', 'Yam'])
Year = st.number_input("Year", min_value=2007, max_value=2030)
Month = st.number_input("Month", min_value=1, max_value=12)
Day = st.number_input("Day", min_value=1, max_value=31)

#Convert categorical values to numbers (Manual Label Encoding)
category_mappings = {
    'Yam': 0, 'Cassava_meal': 1, 'Cowpeas': 2, 'Gari': 3, 'Groundnuts': 4, 'Maize': 5, 'Millet': 6, 'Rice': 7, 'Sorghum': 8
}

#Apply encoding
encoded_data = [
    category_mappings[Product],
    Year,
    Month,
    Day
]

#Convert to Numpy array
input_data = np.array([encoded_data])

#Predict on user input
if st.button("Predict Food Price"):
    prediction = model.predict(input_data)
    st.write(f"Predicted price: {prediction[0]:.2f}")
 

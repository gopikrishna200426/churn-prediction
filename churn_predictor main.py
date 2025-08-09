import pandas as pd
import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'Churn_prediction_model')
model = joblib.load(model_path)
# Reverse encoding 
geography_mapping = {0: "France", 1: "Spain", 2: "Germany"}
gender_mapping = {0: "Female", 1: "Male"}

def main():
    st.title("Churn Predictor Model")
    # creating input fields
    CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, step=1)
    Geography = st.selectbox("Geography", options=list(geography_mapping.keys()), 
                             format_func=lambda x: geography_mapping[x])
    Gender = st.selectbox("Gender", options=list(gender_mapping.keys()), 
                          format_func=lambda x: gender_mapping[x])
    Age = st.number_input("Age", min_value=18, max_value=100, step=1)
    Tenure = st.number_input("Tenure", min_value=0, max_value=10, step=1)
    Balance = st.number_input("Balance", min_value=0.0, step=0.01)
    NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4, step=1)
    HasCrCard = st.selectbox("Has Credit Card", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    IsActiveMember = st.selectbox("Is Active Member", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, step=0.01)
        
    # Create a dataframe from the input values
    input_data = pd.DataFrame({
    'CreditScore': [CreditScore],  
    'Geography': [Geography], 
    'Gender': [Gender],  
    'Age': [Age],
    'Tenure': [Tenure],
    'Balance' : [Balance],
    'NumOfProducts': [NumOfProducts], 
    'HasCrCard': [HasCrCard], 
    'IsActiveMember': [IsActiveMember],
    'EstimatedSalary': [EstimatedSalary] 
        
    })
    if st.button("Predict"):
        with st.spinner('Calculating...'):  # Display a spinner while predicting
            prediction = model.predict(input_data)
            st.success(f"Predicted churn: {prediction[0]:,.2f}")  # Access the prediction value correctly
            st.balloons()

# Run the app
if __name__ == "__main__":
  main()

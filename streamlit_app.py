import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and columns
model = joblib.load('xgb_salary_model.pkl')

# Load the columns used for training
# You can save your X.columns as a list in a file, or hardcode here
model_features = joblib.load('model_features.pkl')

st.title("Employee Salary Predictor (ML Powered)")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=65, value=30)
exp = st.number_input("Years of Experience", min_value=0, max_value=40, value=5)
gender = st.selectbox("Gender", ["Male", "Female"])
edu = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job = st.selectbox("Job Title", [
    'Data Analyst', 'Director', 'Financial Analyst', 'IT Support', 'Marketing Analyst', 'Marketing Manager',
    'Product Manager', 'Sales Associate', 'Sales Manager', 'Software Developer', 'Software Engineer', 'Senior Manager'
    # ...add all unique job titles from your dataset
])

# Prepare input for model
input_dict = {col: 0 for col in model_features}
input_dict['Age'] = age
input_dict['Years of Experience'] = exp
if gender == "Male":
    input_dict['Gender_Male'] = 1
if edu == "Master's":
    input_dict["Education Level_Master's"] = 1
elif edu == "PhD":
    input_dict["Education Level_PhD"] = 1
job_col = f"Job Title_{job}"
if job_col in input_dict:
    input_dict[job_col] = 1

input_df = pd.DataFrame([input_dict])
input_df = input_df[model_features]  # Ensure order

if st.button("Predict Salary"):
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Salary: ₹{pred:,.0f}")
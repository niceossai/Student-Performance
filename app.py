import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model_student.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="🎓 Student Performance Predictor")
st.title("🎓 Student Performance Prediction App")
st.markdown("Enter the student's details below:")

# Input fields
hours_studied = st.slider("Hours Studied", 0.0, 12.0, step=0.5)
previous_scores = st.slider("Previous Scores (out of 100)", 0.0, 100.0, step=1.0)
sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, step=0.5)
sample_questions = st.number_input("Sample Question Papers Practiced", min_value=0, step=1)

extracurricular = st.radio(
    "Do they participate in extracurricular activities?",
    ("Yes", "No")
)

# Convert radio to encoded variables
if extracurricular == "Yes":
    extra_no = 0
    extra_yes = 1
else:
    extra_no = 1
    extra_yes = 0

# Collect features into a list
features = np.array([[hours_studied, previous_scores, sleep_hours,
                      sample_questions, extra_no, extra_yes]])

# Predict button
if st.button("Predict Performance"):
    prediction = model.predict(features)
    st.success(f"🎯 Predicted Performance Score: {round(prediction[0], 2)}")

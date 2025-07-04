# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Medical Insurance Premium Predictor")

st.title("🏥 Insurance Premium Predictor")
st.write("Fill the details below to get the estimated premium:")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, step=1)
diabetes = st.selectbox("Diabetes", [0, 1])
bp = st.selectbox("Blood Pressure Problems", [0, 1])
transplant = st.selectbox("Any Transplants", [0, 1])
chronic = st.selectbox("Any Chronic Diseases", [0, 1])
height = st.number_input("Height (cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300)
allergies = st.selectbox("Known Allergies", [0, 1])
cancer = st.selectbox("History of Cancer in Family", [0, 1])
surgeries = st.slider("Number of Major Surgeries", 0, 10)

if st.button("Predict"):
    input_data = {
        "Age": age,
        "Diabetes": diabetes,
        "BloodPressureProblems": bp,
        "AnyTransplants": transplant,
        "AnyChronicDiseases": chronic,
        "Height": height,
        "Weight": weight,
        "KnownAllergies": allergies,
        "HistoryOfCancerInFamily": cancer,
        "NumberOfMajorSurgeries": surgeries
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        result = response.json()
        st.success(f"💰 Predicted Premium: ₹{result['Predicted Premium Price']}")
    except:
        st.error("❌ Could not connect to the backend API.")

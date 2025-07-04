# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the saved model
model = joblib.load("premium_model.pkl")

# Define FastAPI app
app = FastAPI()

# Request body format
class InsuranceData(BaseModel):
    Age: int
    Diabetes: int
    BloodPressureProblems: int
    AnyTransplants: int
    AnyChronicDiseases: int
    Height: int
    Weight: int
    KnownAllergies: int
    HistoryOfCancerInFamily: int
    NumberOfMajorSurgeries: int


@app.post("/predict")
def predict(data: InsuranceData):
    input_data = [[
        data.Age, data.Diabetes, data.BloodPressureProblems, data.AnyTransplants,
        data.AnyChronicDiseases, data.Height, data.Weight, data.KnownAllergies,
        data.HistoryOfCancerInFamily, data.NumberOfMajorSurgeries
    ]]
    prediction = model.predict(input_data)[0]
    return {"Predicted Premium Price": round(prediction, 2)}

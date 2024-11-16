from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import uvicorn

app = FastAPI(title="Diabetes Prediction API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# Define input data schema
class DiabetesInput(BaseModel):
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.post("/predict/")
def predict_diabetes(input_data: DiabetesInput):
    pred = random.random()
    return {
        "prediction": "Diabetic" if pred > 0.5 else "Non-Diabetic",
        "probability": round(pred, 2),
    }


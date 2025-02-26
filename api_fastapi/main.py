from fastapi import FastAPI 
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load('model_training/model/fraud_detection_model.pkl')

# Define input data structure
class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount_Log: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Real Time Fraud Detection in Financial Transactions by European cardholders API"}

@app.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.dict().values()], columns=transaction.dict().keys())
    prediction = model.predict(data)
    result = "Fraud" if prediction[0] == 1 else "Normal transaction"
    return {"Prediction": result}

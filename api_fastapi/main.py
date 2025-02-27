from fastapi import FastAPI 
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import os 

# Load trained model

model_path = 'model_training/model/fraud_detection_model.pkl'

if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model does not exist in the location : {model_path}")

model = joblib.load(model_path)
print("Model loaded successfully!")
print("Columns expected by the model:", model.feature_names_in_)


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
    Amount: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Real Time Fraud Detection in Financial Transactions by European cardholders API"}

@app.post("/predict")
def predict(transaction: Transaction):
    try:
        data = pd.DataFrame([transaction.dict().values()], columns=transaction.dict().keys())

        # Check if “Amount” is present before transformation
        if "Amount" in data.columns:
            data["Amount_Log"] = np.log1p(data["Amount"])  # Add Amount_Log
        
        print("Dataset after transformation :", data.head())  # Debugging


        # Prediction
        prediction = model.predict(data)
        probability = model.predict_proba(data)[:, 1]  # Fraud Probability

        result = "Fraud" if prediction[0] == 1 else "Normal transaction"

        return {"Prediction": result, "Probability": float(probability[0])}


    except Exception as e:
        print("Error :", str(e))
        return {"error": str(e)}

# launch in terminal : python -m uvicorn api_fastapi.main:app --host 0.0.0.0 --port 8000 --reload
# http://127.0.0.1:8000/docs : test the /predict endpoint directly by sending a POST request.

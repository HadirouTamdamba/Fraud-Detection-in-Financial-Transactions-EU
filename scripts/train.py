import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import xgboost as xgb
from imblearn.over_sampling import SMOTE
import joblib

# Load data
data = pd.read_csv("data/creditcard.csv")

# Preprocessing
X = data.drop("Class", axis=1)
y = data["Class"]

# Class imbalance management with SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Model Comparisons
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "XGBoost": xgb.XGBClassifier(n_estimators=100, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    roc_auc = roc_auc_score(y_test, y_pred)
    results[name] = roc_auc
    print(f"{name} - ROC AUC: {roc_auc}")

# Saving the best data 
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
best_model
print(best_model)
joblib.dump(best_model, "models/best_fraud_detection_model.pkl") 
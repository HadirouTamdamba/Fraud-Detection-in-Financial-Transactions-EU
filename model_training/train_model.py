import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE
import joblib
import os

#  Upload data preprocessed
def load_data():
    X_train = pd.read_csv('data_pipeline/processed_data/X_train.csv')
    X_test = pd.read_csv('data_pipeline/processed_data/X_test.csv')
    y_train = pd.read_csv('data_pipeline/processed_data/y_train.csv')
    y_test = pd.read_csv('data_pipeline/processed_data/y_test.csv')
    return X_train, X_test, y_train.values.ravel(), y_test.values.ravel()

# Applying SMOTE to balance classes
def balance_data(X_train, y_train):
    smote = SMOTE(sampling_strategy=0.1, random_state=42)  # With sampling_strategy=0.1, we adjust the number of frauds to 10% of the number of normal transactions. 
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
    print(" Distribution after SMOTE:\n", pd.Series(y_resampled).value_counts())
    return X_resampled, y_resampled

# Model training
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

#  Evaluation of the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nAccuracy:", accuracy_score(y_test, y_pred))

#  Saving model
def save_model(model, model_path='model_training/model/fraud_detection_model.pkl'):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f" Model saved at location : {model_path}")

#  Main Pipeline
def model_pipeline():
    X_train, X_test, y_train, y_test = load_data()

    #  Applying SMOTE to balance classes
    X_train_balanced, y_train_balanced = balance_data(X_train, y_train)

    #  Training the model with balanced data
    model = train_model(X_train_balanced, y_train_balanced)
    
    # Model evaluation
    evaluate_model(model, X_test, y_test)

    # Saving model
    save_model(model)

if __name__ == '__main__':
    model_pipeline()

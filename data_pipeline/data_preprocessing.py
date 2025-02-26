import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

# Load YAML configuration
def load_config(config_path='data_pipeline/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Upload dataset
def load_dataset(file_path='data/creditcard.csv'):
    return pd.read_csv(file_path)

# Column deletion
def drop_columns(df, columns):
    return df.drop(columns=columns, axis=1)

# Column normalization
def normalize_columns(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

# Logarithmic transformation
def log_transform(df, columns):
    for col in columns:
        df[col+'_Log'] = np.log1p(df[col])
    return df

# Data Split 
def split_data(df, test_size=0.2, random_state=42):
    X = df.drop('Class', axis=1)
    y = df['Class']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Main Pipeline 
def data_pipeline():
    config = load_config()
    df = load_dataset()
    
    # Column deletion
    df = drop_columns(df, config['preprocessing']['drop_columns'])
    
    # Normalization
    df = normalize_columns(df, config['preprocessing']['normalize_columns'])
    
    # Logarithmic Transformation 
    df = log_transform(df, config['preprocessing']['log_transform_columns'])
    
    # Data Split
    X_train, X_test, y_train, y_test = split_data(df, 
                                                  config['preprocessing']['split']['test_size'], 
                                                  config['preprocessing']['split']['random_state'])
    
    # Saving pre-processed datasets
    os.makedirs('data_pipeline/processed_data', exist_ok=True)
    X_train.to_csv('data_pipeline/processed_data/X_train.csv', index=False)
    X_test.to_csv('data_pipeline/processed_data/X_test.csv', index=False)
    y_train.to_csv('data_pipeline/processed_data/y_train.csv', index=False)
    y_test.to_csv('data_pipeline/processed_data/y_test.csv', index=False)
    print("Data successfully preprocessed and saved.")

if __name__ == '__main__':
    data_pipeline() 

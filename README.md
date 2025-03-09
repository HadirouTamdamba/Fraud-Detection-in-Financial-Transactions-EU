
# Fraud Detection in Financial Transactions by European Cardholders

[![GitHub issues](https://img.shields.io/github/issues/HadirouTamdamba/Fraud-Detection-in-Financial-Transactions-EU)](https://github.com/HadirouTamdamba/Fraud-Detection-in-Financial-Transactions-EU/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This project demonstrates a complete end-to-end system for detecting fraudulent transactions using Machine Learning. The solution comprises an automated data pipeline, a Machine Learning model deployed via FastAPI on Render, and an interactive user interface built with Streamlit and hosted on GitHub Pages. This project showcases skills in data preprocessing, model training (with imbalance handling), API development, and cloud deployment.

---

## Problem Statement

The goal is to detect fraudulent transactions in a dataset of credit card transactions. Financial institutions can use this system to reduce fraud risk and improve their security systems.

---

## Dataset Description

The project uses the **Credit Card Fraud Detection** dataset from Kaggle, which contains 284,807 credit card transactions, of which 492 are fraudulent. The dataset is highly imbalanced, and the features (V1 to V28) are anonymized, along with the transaction amount.

- **Source:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## Exploratory Data Analysis (EDA)

- **Class Distribution:** The dataset shows a significant imbalance between normal and fraudulent transactions.
- **Amount Distribution:** The transaction amount is also analyzed, with a log transformation applied to manage skewness.

---

## Modeling

### Data Pipeline
- **Automated Data Pipeline:** Implemented using a YAML configuration file to manage data cleaning, normalization, and log transformation.
- **Techniques Used:** 
  - **Column Deletion:** Removing unnecessary columns (e.g., Time).
  - **Normalization:** Applying standard scaling to continuous features.
  - **Log Transformation:** Transforming the 'Amount' variable to 'Amount_Log' for better handling of skewness.
  
### Model Training
- **Random Forest Classifier:** Chosen for its robustness and speed in prediction, especially when dealing with imbalanced data.
- **Imbalance Handling:** SMOTE (Synthetic Minority Over-sampling Technique) was applied to generate synthetic samples for the minority class, improving recall for fraudulent transactions.
  
**Why Random Forest?**  
Due to the extreme imbalance in the dataset, most models tend to favor the majority class. Random Forest, combined with SMOTE, provides a balanced approach between precision and recall. It achieves high accuracy while ensuring that the minority (fraud) class is adequately represented.

---

## Evaluation

The best model was evaluated on the test data, and the following results were obtained:

**Distribution after SMOTE:**

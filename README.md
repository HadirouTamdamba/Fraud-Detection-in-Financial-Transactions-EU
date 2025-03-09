# Fraud Detection in Financial Transactions by European cardholders
Link to database : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Problem Statement
The goal is to detect fraudulent transactions in a dataset of credit card transactions. This project is useful for banks and financial institutions.

## Dataset Description
The **Credit Card Fraud Detection** dataset contains 284,807 transactions, of which 492 are fraudulent. The variables are anonymized (V1 to V28) and include the transaction amount.

## Exploratory Data Analysis (EDA)
- Distribution of classes.
- Distribution of amounts.

## Modeling

- **Random Forest**


## Evaluation
The best model is selected based on **ROC AUC**.

## Deployment
A Fast API is created to detect fraud in real-time.

## Conclusion
The **Random Forest** model achieved the best performance with a ROC AUC of 0.90. This project demonstrates how AI can help prevent financial fraud.

import streamlit as st
import requests
import json
import pandas as pd

# API URL Configuration

API_URL = "https://project-fraud-detection-in-financial.onrender.com/predict"

# Store transaction history
if "history" not in st.session_state:
    st.session_state.history = []
 
# Application Title
st.title("💳 Real Time Fraud Detection in Financial Transactions by European Cardholders")

# Description
st.markdown("Enter the transaction features to check whether it is fraudulent or normal.")

# Creating input fields for features
features = {}

for i in range(1, 29):
    features[f"V{i}"] = st.number_input(f"V{i}", value=0.0)

features["Amount"] = st.number_input("Transaction Amount (€)", value=10.0)

# Button to trigger prediction
if st.button("Predict"):
    try:
        # Send POST request to FastAPI
        response = requests.post(API_URL, data=json.dumps(features), headers={"Content-Type": "application/json"})

        # Check response status
        if response.status_code == 200:
            result = response.json()
            prediction = result["Prediction"]
            probability = result.get("Probability", None)  # Retrieve probability if available

            # Save to history
            transaction_data = {**features, "Prediction": prediction, "Probability": probability}
            st.session_state.history.append(transaction_data)

            # Display result
            if probability:
                st.success(f"🟢 Result: **{prediction}** with a probability of **{probability*100:.2f}%**")
            else:
                st.success(f"🟢 Result: **{prediction}**")

        else:
            st.error("❌ Error during prediction, please check the API.")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display transaction history
st.subheader("📜 Analyzed Transactions History")
if len(st.session_state.history) > 0:
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history) 
else:
    st.info("No transactions analyzed yet.")

# About the Author Section
st.markdown("""
---
### 👨‍💻 About the Author
**Hadirou Tamdamba**  
AI Engineer Data Scientist Associate | MLOps Engineer  

🔗 [LinkedIn](https://www.linkedin.com/in/hadirou-tamdamba/)  
🔗 [GitHub](https://github.com/HadirouTamdamba)  
""", unsafe_allow_html=True) 


# Launching on terminal: streamlit run "d:/Mon Portfolio Projets/Project_Fraud-Detection-in-Financial-Transactions-EU/frontend_streamlit/app_streamlit.py"
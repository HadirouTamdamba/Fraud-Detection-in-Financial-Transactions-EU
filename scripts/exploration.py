import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data 
data = pd.read_csv("data/creditcard.csv")

# Class distribution
plt.figure(figsize=(10, 6))
sns.countplot(x="Class", data=data)
plt.title("Transaction distribution (0: Normal, 1: Fraud)")
plt.xlabel("Class")
plt.ylabel("Number of transactions")
plt.show()

# Amount distribution 
plt.figure(figsize=(10, 6))
sns.histplot(data[data["Class"] == 0]["Amount"], bins=50, color="blue", label="Normale")
sns.histplot(data[data["Class"] == 1]["Amount"], bins=50, color="red", label="Fraude")
plt.legend()
plt.title("Amount distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show() 
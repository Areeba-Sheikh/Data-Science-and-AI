import pandas as pd
import numpy as np

from pandas_profiling import ProfileReport

df = pd.read_csv("telecom_customer_churn.csv")
print(df)

# Generating a profiling report
profile = ProfileReport(df)
profile.to_file(output_file="Telecom Customer Churn Report.html")

print("Shape:", df.shape)
num_duplicates = df.duplicated().sum()
print("Number of duplicates:", num_duplicates)
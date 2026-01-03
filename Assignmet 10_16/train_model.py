"""
Week 9-13: Train and save model for deployment
Simple script to train a RandomForest classifier and save it.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('telecom_customer_churn_cleaned.csv')
print(f"Dataset shape: {df.shape}")

# Find target column (Churn, Customer Status, etc.)
target_candidates = ['Customer Status', 'Churn', 'Exited', 'Target']
target_col = None
for col in target_candidates:
    if col in df.columns:
        target_col = col
        break

if not target_col:
    raise KeyError("Could not find target column (Churn, Customer Status, etc.). Check your dataset.")

print(f"Target column: {target_col}")

# Encode target
le = LabelEncoder()
df[target_col] = le.fit_transform(df[target_col])

# Features: drop target, encode categorical
X = df.drop(columns=[target_col])
X = pd.get_dummies(X, drop_first=True)
y = df[target_col]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
accuracy = model.score(X_test_scaled, y_test)
print(f"Model Accuracy: {accuracy:.4f}")

# Save model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(X.columns.tolist(), 'feature_columns.pkl')

print("✅ Model saved to model.pkl, scaler.pkl, and feature_columns.pkl")

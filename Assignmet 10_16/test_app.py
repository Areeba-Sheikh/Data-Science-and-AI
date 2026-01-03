"""Test Flask app using TestClient (no server needed)"""
import json
import joblib
from app import app

client = app.test_client()

# Load feature columns to build test payload
feature_columns = joblib.load('feature_columns.pkl')

# Build sample input
test_input = {
    'features': {col: 0 for col in feature_columns[:20]}  # Use first 20 features, set to 0
}

print("🧪 Testing Flask app...")
response = client.post('/predict', json=test_input)
print(f"✅ Status: {response.status_code}")
result = response.get_json()
print(f"📊 Response:\n{json.dumps(result, indent=2)}")

"""Quick test of Flask app predictions"""
import requests
import json
import joblib
import subprocess
import time
import sys

# Start Flask app in background
print("Starting Flask app...")
proc = subprocess.Popen([sys.executable, 'app.py'], 
                       stdout=subprocess.DEVNULL, 
                       stderr=subprocess.DEVNULL)
time.sleep(2)

try:
    # Load feature columns to build test payload
    feature_columns = joblib.load('feature_columns.pkl')
    
    # Build sample input
    test_input = {
        'features': {col: 0 for col in feature_columns[:20]}  # Use first 20 features, set to 0
    }
    
    # Make prediction request
    response = requests.post('http://127.0.0.1:5000/predict', json=test_input)
    print(f"✅ Status: {response.status_code}")
    print(f"📊 Response: {json.dumps(response.json(), indent=2)}")
    
finally:
    proc.terminate()
    proc.wait()

import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "features": {"Gender": 0, "Age": 35, "Married": 0}
}

response = requests.post(url, json=data)

# Debugging output
print("Status code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception:
    print("Raw response text:", response.text)

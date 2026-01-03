"""
Week 13: Simple Flask app to serve predictions on localhost
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model, scaler, feature columns
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'Model server is running',
        'endpoint': '/predict'
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    POST endpoint to make predictions.

    Expected JSON:
    {
        "features": {
            "tenure": 24,
            "MonthlyCharges": 65.5,
            "Contract_Month-to-month": 1,
            ...
        }
    }
    """
    try:
        data = request.json['features']

        # Build feature array in training order
        feature_values = [data.get(col, 0) for col in feature_columns]

        feature_array = np.array(feature_values).reshape(1, -1)
        feature_scaled = scaler.transform(feature_array)

        # Model prediction
        pred_class = int(model.predict(feature_scaled)[0])
        probs = model.predict_proba(feature_scaled)[0]
        confidence = float(probs[pred_class])

        # ---- USER FRIENDLY LOGIC ----
        if pred_class == 0:
            prediction_label = "No Churn"
            risk_level = "Low"
            message = "Customer is unlikely to churn"
        else:
            prediction_label = "Churn"
            risk_level = "High"
            message = "Customer is likely to churn"

        return jsonify({
            "prediction": prediction_label,
            "confidence": f"{confidence * 100:.2f}%",
            "risk_level": risk_level,
            "message": message
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)

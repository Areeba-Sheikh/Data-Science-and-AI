# Telecom Customer Churn Prediction

A machine learning project that predicts customer churn for a telecom company using a trained Random Forest classifier, exposed through a Flask REST API.

## Project Overview

This project builds a predictive model to identify customers likely to churn (leave the telecom service). The model is trained on historical customer data and deployed as a REST API endpoint for real-time predictions.

**Key Features:**
- Binary classification (Churn / No Churn)
- Random Forest model with high accuracy
- Scaled features for optimal predictions
- REST API for easy integration
- Human-friendly output with confidence scores and risk assessment

## Project Structure

```
.
├── app.py                              # Flask application with /predict endpoint
├── train_model.py                      # Model training script
├── DSproject.ipynb                     # Jupyter notebook with EDA and analysis
├── preprocessor.joblib                 # Feature preprocessor (serialized)
├── rf_model.joblib                     # Trained Random Forest model
├── scaler.joblib                       # Feature scaler (StandardScaler)
├── telecom_customer_churn_cleaned.csv  # Training dataset
├── requirements.txt                    # Python dependencies
├── test_app.py                         # Unit tests for Flask app
├── test_request.py                     # API integration tests
├── quick_test.py                       # Quick manual testing script
└── README.md                           # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project:**
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Flask API

1. **Start the server:**
   ```bash
   python app.py
   ```

   The server will start on `http://127.0.0.1:5000/`

2. **Test the API:**

   **GET request (health check):**
   ```bash
   curl http://127.0.0.1:5000/
   ```

   **POST request (prediction):**
   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
       "features": {
         "tenure": 24,
         "MonthlyCharges": 65.5,
         "Contract_Month-to-month": 1,
         "Contract_One year": 0,
         "Contract_Two year": 0
       }
     }'
   ```

### Example API Response

**Request:**
```json
{
  "features": {
    "tenure": 24,
    "MonthlyCharges": 65.5,
    "Contract_Month-to-month": 1
  }
}
```

**Response:**
```json
{
  "prediction": "No Churn",
  "confidence": "91.00%",
  "risk_level": "Low",
  "message": "Customer is unlikely to churn"
}
```

## Model Details

- **Algorithm:** Random Forest Classifier
- **Training Data:** Telecom customer churn dataset
- **Features:** 20+ customer attributes (tenure, charges, contract type, services, etc.)
- **Target:** Binary (0 = No Churn, 1 = Churn)
- **Preprocessing:** StandardScaler normalization

### Features Tracked

The model uses the following customer features for prediction:
- Demographic: Age, gender
- Account: Tenure, contract type, billing method
- Services: Internet, phone, streaming services, security, support
- Charges: Monthly and total charges

## API Endpoints

### GET `/`
Health check endpoint.

**Response:**
```json
{
  "status": "Model server is running",
  "endpoint": "/predict"
}
```

### POST `/predict`
Make predictions on customer churn.

**Request Format:**
```json
{
  "features": {
    "feature_name_1": value,
    "feature_name_2": value,
    ...
  }
}
```

**Response Format:**
```json
{
  "prediction": "Churn" | "No Churn",
  "confidence": "X.XX%",
  "risk_level": "Low" | "High",
  "message": "Description of prediction"
}
```

## Testing

Run unit tests to verify the API functionality:

```bash
# Install pytest if not already installed
pip install pytest

# Run tests
python -m pytest -q
```

Or manually test with the provided scripts:
```bash
python quick_test.py
python test_request.py
```

## Data

The dataset (`telecom_customer_churn_cleaned.csv`) contains:
- **Rows:** Customer records
- **Columns:** Features and target variable (Churn)
- **Status:** Pre-cleaned and preprocessed

## Model Training

To retrain the model with new data:

```bash
python train_model.py
```

This script will:
1. Load and preprocess the data
2. Split into train/test sets
3. Train the Random Forest model
4. Save the model, scaler, and preprocessor to `.joblib` files

## Dependencies

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning library
- **joblib** - Model serialization
- **flask** - Web framework for REST API
- **matplotlib** - Data visualization
- **shap** - Model explainability

See `requirements.txt` for specific versions.

## Exploratory Data Analysis

Open `DSproject.ipynb` in Jupyter Notebook to explore:
- Data distribution
- Feature correlations
- Model performance metrics
- Feature importance analysis

```bash
jupyter notebook DSproject.ipynb
```

## Performance Metrics

The model achieves strong performance on the test set. For detailed metrics, see the Jupyter notebook or run:

```bash
python train_model.py
```

## Error Handling

The API includes error handling for:
- Invalid JSON format
- Missing required fields
- Unexpected feature values

Errors return a JSON response with an error message and HTTP 400 status.

## Deployment Notes

For production deployment:
1. Set `debug=False` (already configured)
2. Use a production WSGI server (e.g., Gunicorn)
3. Add authentication if needed
4. Implement rate limiting
5. Add logging and monitoring

## Course Coverage (Weeks 1–16)

- **Weeks 1–8**: Data cleaning, visualization, stats, regression, classification, evaluation, clustering (in notebook)
- **Weeks 9–13**: Model deployment, Flask API, REST endpoints, containerization concepts
- **Weeks 14–16**: Production considerations, documentation, testing, version control

All work is documented in `DSproject.ipynb`

## Contributors

Assignment submission for Machine Learning course

## Support

For issues or questions about the project, please refer to the code comments and the Jupyter notebook (`DSproject.ipynb`) for detailed explanations.



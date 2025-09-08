
from flask import Flask, request, jsonify, abort
import joblib
import pandas as pd
import logging
import os

app = Flask(__name__)
model = joblib.load('C:/Project/credit-card-fraud-detection/data/fraud_model.pkl')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
API_KEY = os.environ.get('API_KEY', 'mysecretkey')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

def validate_api_key():
    if request.headers.get('x-api-key') != API_KEY:
        abort(401, description='Invalid API key')

def validate_input(data):
    required = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    missing = [k for k in required if k not in data]
    if missing:
        abort(400, description=f'Missing keys: {missing}')

@app.route('/predict', methods=['POST'])
def predict():
    validate_api_key()
    data = request.get_json(force=True)
    validate_input(data)
    try:
        pred = model.predict(pd.DataFrame([data]))
        logging.info(f'Prediction: {pred[0]}')
        return jsonify({'fraud': bool(pred[0])})
    except Exception as e:
        logging.error(f'Prediction error: {str(e)}')
        abort(500, description=str(e))

@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    validate_api_key()
    data = request.get_json(force=True)
    if not isinstance(data, list):
        abort(400, description='Input should be a list of records')
    for record in data:
        validate_input(record)
    try:
        preds = model.predict(pd.DataFrame(data))
        logging.info(f'Batch prediction: {len(preds)} records')
        return jsonify({'fraud': [bool(p) for p in preds]})
    except Exception as e:
        logging.error(f'Batch prediction error: {str(e)}')
        abort(500, description=str(e))

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': str(error)}), 401

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)

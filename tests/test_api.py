import requests
import os

API_URL = 'http://127.0.0.1:5000/predict'
API_BATCH_URL = 'http://127.0.0.1:5000/predict_batch'
HEALTH_URL = 'http://127.0.0.1:5000/health'
API_KEY = os.environ.get('API_KEY', 'mysecretkey')

headers = {'x-api-key': API_KEY}

sample_payload = {
    "Time": 10000,
    "V1": -1.3598071336738,
    "V2": 1.19185711131486,
    "V3": -0.358354,
    "V4": 0.12345,
    "V5": -0.6789,
    "V6": 0.9876,
    "V7": -0.1234,
    "V8": 0.5678,
    "V9": -0.2345,
    "V10": 0.3456,
    "V11": -0.4567,
    "V12": 0.5678,
    "V13": -0.6789,
    "V14": 0.7890,
    "V15": -0.8901,
    "V16": 0.9012,
    "V17": -0.1234,
    "V18": 0.2345,
    "V19": -0.3456,
    "V20": 0.4567,
    "V21": -0.5678,
    "V22": 0.6789,
    "V23": -0.7890,
    "V24": 0.8901,
    "V25": -0.9012,
    "V26": 0.1234,
    "V27": -0.2345,
    "V28": 0.3456,
    "Amount": 149.62
}

def test_health():
    r = requests.get(HEALTH_URL)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    r = requests.post(API_URL, json=sample_payload, headers=headers)
    assert r.status_code == 200
    assert "fraud" in r.json()

def test_predict_batch():
    batch = [sample_payload, sample_payload]
    r = requests.post(API_BATCH_URL, json=batch, headers=headers)
    assert r.status_code == 200
    assert "fraud" in r.json()
    assert isinstance(r.json()["fraud"], list)

if __name__ == "__main__":
    test_health()
    test_predict()
    test_predict_batch()
    print("All API tests passed!")

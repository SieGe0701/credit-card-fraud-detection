import streamlit as st
import requests
import os
import json

API_URL = 'http://127.0.0.1:5000/predict'
API_KEY = os.environ.get('API_KEY', 'mysecretkey')

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("Credit Card Fraud Detection")
st.markdown("Enter transaction details below or paste a JSON payload.")

FEATURE_KEYS = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

with st.form("form_input"):
    st.subheader("Form Input")
    form_data = {}
    for key in FEATURE_KEYS:
        form_data[key] = st.number_input(key, value=0.0, format="%f")
    submitted = st.form_submit_button("Predict (Form)")
    if submitted:
        headers = {'x-api-key': API_KEY}
        response = requests.post(API_URL, json=form_data, headers=headers)
        result = response.json().get('fraud', 'Error')
        st.success(f"Fraud: {result}")

st.subheader("Raw JSON Input")
json_payload = st.text_area("Paste JSON payload here", value=json.dumps({k: 0.0 for k in FEATURE_KEYS}, indent=2))
if st.button("Predict (JSON)"):
    try:
        payload = json.loads(json_payload)
        headers = {'x-api-key': API_KEY}
        response = requests.post(API_URL, json=payload, headers=headers)
        result = response.json().get('fraud', 'Error')
        st.success(f"Fraud: {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

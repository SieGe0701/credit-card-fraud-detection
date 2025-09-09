
# Credit Card Fraud Detection

This project is a full-fledged credit card fraud detection system using Python, pandas, scikit-learn, Flask, and Streamlit. It supports model training, API predictions, and a modern web UI.

## Project Structure
- `data/` — Store datasets and trained models
- `notebooks/` — Jupyter notebooks for EDA
- `src/` — Source code for preprocessing, training, API, and Streamlit UI
- `docs/` — Documentation
- `Dockerfile`, `Dockerfile.api`, `docker-compose.yml` — Deployment files

## Getting Started
1. Place your dataset (e.g., `creditcard.csv`) in the `data/` folder.
2. Run preprocessing and training scripts in `src/` to build the model:
	- `python src/preprocess.py`
	- `python src/train_model.py`
3. Start the Flask API:
	- `python src/app.py` (or deploy with Docker/Cloud Run)
4. Start the Streamlit UI:
	- `streamlit run src/streamlit_app.py`
5. Use the web UI or API endpoints for predictions.

## Deployment
- **Local:** Use Docker Compose to run both API and UI:
  ```sh
  docker-compose up --build
  ```
- **Google Cloud Run:** Deploy `Dockerfile.api` and `Dockerfile` as separate services. Update the Streamlit app’s `API_URL` to the public API endpoint.

## Features
- Data preprocessing and class balancing (SMOTE)
- Model training and evaluation (Random Forest)
- REST API for predictions and batch predictions
- Streamlit web UI (form and JSON input)
- Automated tests in `tests/`
- Modern deployment with Docker and Cloud Run

## Enhancements
- Try other models (XGBoost, LightGBM, etc.)
- Add model explainability (SHAP, LIME)
- Add authentication, logging, and monitoring
- Visualize metrics in the UI

## Requirements
- Python 3.8+
- pandas, scikit-learn, Flask, imbalanced-learn, streamlit, requests

---

For details, see the notebooks and scripts in each folder. Contributions welcome!

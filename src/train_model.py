import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

X_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_train.csv')
X_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_test.csv')
y_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_train.csv').values.ravel()
y_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_test.csv').values.ravel()

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
joblib.dump(clf, 'C:/Project/credit-card-fraud-detection/data/fraud_model.pkl')

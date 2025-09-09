import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import cross_val_score
import joblib

X_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_train.csv')
X_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_test.csv')
y_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_train.csv').values.ravel()
y_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_test.csv').values.ravel()

clf = RandomForestClassifier(n_estimators=10, max_depth=8, min_samples_leaf=10, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred_test = clf.predict(X_test)
y_pred_train = clf.predict(X_train)

print("Test Set Classification Report:")
print(classification_report(y_test, y_pred_test))
print("Test Set Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_test))
print("Test Set ROC AUC:", roc_auc_score(y_test, y_pred_test))

print("\nTrain Set Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Train Set Confusion Matrix:")
print(confusion_matrix(y_train, y_pred_train))
print("Train Set ROC AUC:", roc_auc_score(y_train, y_pred_train))

# Cross-validation
cv_scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='roc_auc')
print("\nCross-validation ROC AUC scores:", cv_scores)
print("Mean CV ROC AUC:", cv_scores.mean())

joblib.dump(clf, 'C:/Project/credit-card-fraud-detection/data/models/fraud_model.pkl')
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib

X_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_train.csv')
X_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/X_test.csv')
y_train = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_train.csv').values.ravel()
y_test = pd.read_csv('C:/Project/credit-card-fraud-detection/data/y_test.csv').values.ravel()

clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred_test = clf.predict(X_test)
y_pred_train = clf.predict(X_train)

print("Test Set Classification Report:")
print(classification_report(y_test, y_pred_test))
print("Test Set Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_test))
print("Test Set ROC AUC:", roc_auc_score(y_test, y_pred_test))

print("\nTrain Set Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Train Set Confusion Matrix:")
print(confusion_matrix(y_train, y_pred_train))
print("Train Set ROC AUC:", roc_auc_score(y_train, y_pred_train))

joblib.dump(clf, 'C:/Project/credit-card-fraud-detection/data/models/fraud_model.pkl')

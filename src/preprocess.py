import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = 'C:/Project/credit-card-fraud-detection/data/creditcard.csv'
df = pd.read_csv(DATA_PATH)
X = df.drop('Class', axis=1)
y = df['Class']
X_scaled = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
pd.DataFrame(X_train, columns=X.columns).to_csv('C:/Project/credit-card-fraud-detection/data/X_train.csv', index=False)
pd.DataFrame(X_test, columns=X.columns).to_csv('C:/Project/credit-card-fraud-detection/data/X_test.csv', index=False)
pd.DataFrame(y_train).to_csv('C:/Project/credit-card-fraud-detection/data/y_train.csv', index=False)
pd.DataFrame(y_test).to_csv('C:/Project/credit-card-fraud-detection/data/y_test.csv', index=False)

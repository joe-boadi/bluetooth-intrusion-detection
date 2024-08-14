from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import pandas as pd
from data_cleaning import preprocess_data


# Load the dataset
data = pd.read_csv('bluetooth_data.csv')

X, y = preprocess_data('bluetooth_data1.csv')

# Split the data into features and labels
X = data.drop('label', axis=1)
y = data['label']

# Standardize the features
scaler = StandardScaler()

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
# print(f'Report: {classification_report:.2f}')

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import time

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
print("Splitting dataset")
time.sleep(20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a logistic regression model
model = LogisticRegression(max_iter=200)
print("Fitting dataset")
time.sleep(20)
model.fit(X_train, y_train)

# Make predictions
print("Predicting on test")
time.sleep(10)
y_pred = model.predict(X_test)


# Calculate accuracy
print("Calculating accuracy")
time.sleep(5)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save the model (optional)
print("Saving model")
time.sleep(5)
joblib.dump(model, "model.joblib")

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load the data
df = pd.read_csv("app/data.csv")

# 2. Split into features and target
feature_cols = ["energy_usage", "renewable_pct", "recycling_pct", "green_investments"]
X = df[feature_cols]
y = df["green_score"]

# 3. Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 4. Save the model to disk
joblib.dump(model, "app/green_score_model.pkl")
print("Model trained and saved as app/green_score_model.pkl")

# 5. (Optional) Predict on a sample input and print result
sample_input = pd.DataFrame(
    [[120, 40, 60, 50000]],
    columns=["energy_usage", "renewable_pct", "recycling_pct", "green_investments"]
)
predicted_score = model.predict(sample_input)[0]
print(f"Predicted green score for {sample_input.values[0]}: {predicted_score:.2f}")
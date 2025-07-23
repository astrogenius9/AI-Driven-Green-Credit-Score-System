import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_PATH = "app/green_score_model.pkl"

def train_model():
    # Dummy data, replace with real data as needed
    df = pd.read_csv("app/data.csv")
    X = df.drop(columns=["green_score"])
    y = df["green_score"]
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def get_model():
    if not os.path.exists(MODEL_PATH):
        return train_model()
    return joblib.load(MODEL_PATH)

def predict_score(data: dict):
    model = get_model()
    df = pd.DataFrame([data])
    score = model.predict(df)[0]
    return round(float(score), 2)
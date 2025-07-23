from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_score

app = FastAPI(title="AI-Driven Green Credit Score System")

class InputData(BaseModel):
    energy_usage: float
    renewable_pct: float
    recycling_pct: float
    green_investments: float

@app.post("/predict")
def predict_green_score(data: InputData):
    score = predict_score(data.dict())
    # Clip the score so it's always between 0 and 100
    score = min(max(score, 0), 100)
    return {"green_score": round(score, 2)}
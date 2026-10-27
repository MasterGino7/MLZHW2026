import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open("pipeline.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)


class Lead(BaseModel):
    lead_source: str
    industry: str
    employment_status: str
    location: str
    number_of_courses_viewed: int
    annual_income: float
    interaction_count: int
    lead_score: float

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(lead: Lead):
    lead_dict = lead.model_dump()
    prob = float(pipeline.predict_proba([lead_dict])[0, 1])
    return {
        "conversion_probability": round(prob, 3),
        "conversion": prob >= 0.5
    }
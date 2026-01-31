from fastapi import FastAPI
from conversation import medical_debate

app = FastAPI()

@app.get("/analyze")
def analyze(case: str):
    return medical_debate(case)

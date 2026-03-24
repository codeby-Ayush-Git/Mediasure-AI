from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MediSure AI Running"}

@app.get("/predict")
def predict(symptom: str):
    if "chest pain" in symptom.lower():
        return {"risk": "High", "action": "Visit hospital immediately"}
    elif "fever" in symptom.lower():
        return {"risk": "Medium", "action": "Consult doctor"}
    else:
        return {"risk": "Low", "action": "Home care"}


from fastapi import FastAPI, Depends
from backend.auth import verify_token
from backend.database import init_db
from backend.scraper import scrape_darkweb
from backend.anomaly_detection import detect_anomalies

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/scrape")
async def scrape(token: str = Depends(verify_token)):
    data = scrape_darkweb()
    return {"status": "success", "data": data}

@app.get("/detect")
async def detect():
    anomalies = detect_anomalies()
    return {"anomalies": anomalies}

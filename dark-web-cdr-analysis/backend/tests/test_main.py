from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_scrape():
    response = client.get("/scrape")
    assert response.status_code == 200
    assert "status" in response.json()

def test_anomaly_detection():
    response = client.get("/detect")
    assert response.status_code == 200
    assert "anomalies" in response.json()

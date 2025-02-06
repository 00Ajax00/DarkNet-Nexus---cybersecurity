# tests/test_api.py
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_scrape():
    response = client.get("/scrape")
    assert response.status_code == 200
    assert "data" in response.json()

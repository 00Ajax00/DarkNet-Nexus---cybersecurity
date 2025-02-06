import jwt
from fastapi.testclient import TestClient
from backend.main import app
from backend.auth import SECRET_KEY

client = TestClient(app)

def test_valid_token():
    token = jwt.encode({"user_id": 1}, SECRET_KEY, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/protected-route", headers=headers)
    assert response.status_code == 200

def test_invalid_token():
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/protected-route", headers=headers)
    assert response.status_code == 401

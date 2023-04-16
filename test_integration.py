from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.post("/authenticate", json={"username": "new_user", "password": "12345"}, )
    assert response.status_code == 200

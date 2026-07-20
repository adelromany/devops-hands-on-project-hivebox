from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["version"] == "1.0.0"

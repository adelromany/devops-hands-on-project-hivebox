"""Tests for the main application endpoints."""
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root():
    """Verify the root endpoint returns the expected message."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to HiveBox!"}

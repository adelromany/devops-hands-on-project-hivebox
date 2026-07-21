"""Tests for the /Temperatur endpoint."""
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


mock_data = {
    "name": "Test Box",
    "currentLocation": {
        "coordinates": [31.2357, 30.0444]
    },
    "sensors": [
        {
            "title": "Temperatur",
            "unit": "°C",
            "lastMeasurement": {
                "value": "30.0"
            }
        }
    ]
}


@patch("src.main.fetch_sensebox", new_callable=AsyncMock)
def test_temperature(mock_fetch):
    """Test the /Temperatur endpoint with a mocked fetch_sensebox function."""
    mock_fetch.return_value = mock_data

    response = client.get("/Temperatur?box_name=ID1")

    assert response.status_code == 200

    assert response.json() == {
        "message": (
            "The temperature at "
            "(30.0444, 31.2357) -> "
            "Test Box is 30.0°C"
        )
    }

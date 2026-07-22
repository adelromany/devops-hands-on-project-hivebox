"""the main module for the HiveBox FastAPI application."""
from fastapi import FastAPI, HTTPException
import httpx
from datetime import datetime, timezone, timedelta

app = FastAPI(
    title="HiveBox",
    description="A sample API",
    version="1.0.0",
)

SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]

BASE_URL = "https://api.opensensemap.org/boxes"


async def fetch_sensebox(box_id: str) -> dict:
    """Fetch SenseBox data from the OpenSenseMap API."""
    url = f"{BASE_URL}/{box_id}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


@app.get("/temperature")
async def get_temperature():
    """Return the average temperature of all recent SenseBoxes."""

    temperatures = []

    for box_id in SENSEBOX_IDS:
        data = await fetch_sensebox(box_id)

        sensor = next(
            (s for s in data["sensors"] if s["title"] == "Temperatur"),
            None,
        )

        if sensor is None:
            continue

        measurement = sensor["lastMeasurement"]

        timestamp = datetime.fromisoformat(
            measurement["createdAt"].replace("Z", "+00:00")
        )

        if datetime.now(timezone.utc) - timestamp > timedelta(hours=1):
            continue

        temperatures.append(float(measurement["value"]))

    if not temperatures:
        raise HTTPException(
            status_code=404,
            detail="No recent temperature data found.",
        )

    return {
        "average_temperature": round(
            sum(temperatures) / len(temperatures),
            2,
        ),
        "boxes_used": len(temperatures),
    }


@app.get("/")
def root():
    """Return the root endpoint."""
    return {"message": "Welcome to HiveBox!"}


@app.get("/version")
def version():
    """Return the application version."""
    return {"version": app.version}


@app.get("/health")
def health():
    """Return the health status of the application."""
    return {"status": "ok"}

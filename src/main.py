from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(
    title="HiveBox",
    description="A sample API",
    version="1.0.0",
)

SENSEBOX_IDS = {
    "ID1": "5eba5fbad46fb8001b799786",
    "ID2": "5c21ff8f919bf8001adf2488",
    "ID3": "5ade1acf223bd80019a1011c",
}

BASE_URL = "https://api.opensensemap.org/boxes"


async def fetch_sensebox(box_id: str) -> dict:
    """Fetch SenseBox data from the OpenSenseMap API."""
    url = f"{BASE_URL}/{box_id}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


@app.get("/Temperatur")
async def get_sensebox(box_name: str):
    box_id = SENSEBOX_IDS.get(box_name)

    if not box_id:
        raise HTTPException(status_code=404, detail="Unknown SenseBox")

    data = await fetch_sensebox(box_id)

    location_name = data["name"]
    longitude, latitude = data["currentLocation"]["coordinates"]

    sensor = next(
        (s for s in data["sensors"] if s["title"] == "Temperatur"),
        None,
    )

    if sensor is None:
        raise HTTPException(
            status_code=404,
            detail="Temperature sensor not found",
        )

    return {
        "message": (
            f"The temperature at "
            f"({latitude}, {longitude}) -> "
            f"{location_name} is "
            f"{sensor['lastMeasurement']['value']}{sensor['unit']}"
        )
    }


@app.get("/")
def root():
    return {"message": "Welcome to HiveBox!"}


@app.get("/version")
def version():
    return {"version": app.version}


@app.get("/health")
def health():
    return {"status": "ok"}
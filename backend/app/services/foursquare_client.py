import httpx
from typing import Any

class FoursquareClient:
    BASE = "https://api.foursquare.com/v3/places"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = httpx.AsyncClient(headers={
            "Accept": "application/json",
            "Authorization": self.api_key,
        }, timeout=15.0)

    async def search(self, lat: float, lon: float, radius: int = 1000, categories: str|None = None) -> Any:
        params = {"ll": f"{lat},{lon}", "radius": radius}
        if categories:
            params['categories'] = categories
        resp = await self.client.get(f"{self.BASE}/search", params=params)
        resp.raise_for_status()
        return resp.json()

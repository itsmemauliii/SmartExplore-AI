import requests
from .config import FOURSQUARE_API_KEY, BASE_URL

headers = {
    "Accept": "application/json",
    "Authorization": FOURSQUARE_API_KEY
}

def search_places(query: str, near: str, limit: int = 5):
    url = f"{BASE_URL}/search"
    params = {"query": query, "near": near, "limit": limit}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

import os
from dotenv import load_dotenv

load_dotenv()

FOURSQUARE_API_KEY = os.getenv("FOURSQUARE_API_KEY")
BASE_URL = "https://api.foursquare.com/v3/places"

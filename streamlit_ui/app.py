import streamlit as st
import requests
import os

# Load API key from environment (set this in Hugging Face later)
FOURSQUARE_API_KEY = os.getenv("FOURSQUARE_API_KEY")

BASE_URL = "https://api.foursquare.com/v3/places/search"

st.set_page_config(page_title="SmartExplore AI", layout="wide")

st.title("🌍 SmartExplore AI")
st.write("Find the most relevant places based on your preferences and context!")

# Inputs
location = st.text_input("Enter location (e.g., New York, Paris)", "New York")
query = st.text_input("What are you looking for? (e.g., cafe, museum)", "cafe")
limit = st.slider("Number of results", 1, 20, 5)

if st.button("Find Places"):
    if not FOURSQUARE_API_KEY:
        st.error("API key not set! Please add it as an environment variable.")
    else:
        headers = {
            "Accept": "application/json",
            "Authorization": FOURSQUARE_API_KEY
        }
        params = {
            "query": query,
            "near": location,
            "limit": limit
        }
        try:
            res = requests.get(BASE_URL, headers=headers, params=params)
            data = res.json()
            if "results" in data:
                for place in data["results"]:
                    st.subheader(place["name"])
                    st.write(place.get("location", {}).get("formatted_address", "No address"))
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"Error: {e}")

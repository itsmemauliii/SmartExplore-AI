from fastapi import FastAPI
from app.foursquare_client import search_places
from app.agent import recommend_best_place

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Explorer API is running!"}

@app.get("/recommend")
def recommend(query: str = "restaurant", near: str = "New York"):
    places = search_places(query, near)
    recommendation = recommend_best_place(places)
    return {"recommendation": recommendation, "raw_results": places}

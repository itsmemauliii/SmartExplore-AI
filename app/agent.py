def recommend_best_place(places_json):
    if "results" not in places_json:
        return "No results found."

    places = places_json["results"]
    # Simple rule: pick the first one (Foursquare sorts by relevance)
    best_place = places[0]

    name = best_place.get("name", "Unknown")
    address = best_place.get("location", {}).get("formatted_address", "No address")
    category = best_place["categories"][0]["name"] if best_place.get("categories") else "General"

    return f"🌟 Recommended: {name}\n📍 Address: {address}\n🍴 Type: {category}"

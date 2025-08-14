from fastapi import FastAPI
from app.api.v1 import routes, health
from app.core.config import settings

app = FastAPI(title="SmartExplore AI - Backend")

app.include_router(health.router, prefix="/health")
app.include_router(routes.router, prefix="/api/v1")

@app.on_event("startup")
async def on_startup():
    # initialize clients, caches, models
    from app.services.foursquare_client import FoursquareClient
    from app.services.recommender import Recommender
    app.state.fs = FoursquareClient(api_key=settings.FOURSQUARE_API_KEY)
    app.state.recommender = Recommender(app.state.fs)

@app.get("/")
async def root():
    return {"message": "SmartExplore AI backend is alive"}

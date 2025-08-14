from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

class SuggestRequest(BaseModel):
    lat: float
    lon: float
    time_iso: str | None = None
    mood_text: str | None = None
    radius_m: int = 1000

@router.post('/suggest')
async def suggest(req: SuggestRequest, request: Request):
    recommender = request.app.state.recommender
    input_ctx = req.dict()
    suggestions = await recommender.suggest(input_ctx)
    return {"results": suggestions}

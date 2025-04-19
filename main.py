
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from services.weather import get_weather_mood
from services.music import get_song_for_mood

class RecommendationRequest(BaseModel):
    city: str = Field(..., example="London")
    mood: str = Field(..., example="happy")

class RecommendationResponse(BaseModel):
    mood_match: bool
    city_weather: str
    recommended_song: dict

app = FastAPI(title="Mood-Weather Music Recommender", version="1.0.0")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(req: RecommendationRequest):
    try:
        weather_mood, weather_desc = await get_weather_mood(req.city)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    mood_match = req.mood.lower() == weather_mood
    try:
        song = await get_song_for_mood(req.mood)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return RecommendationResponse(
        mood_match=mood_match,
        city_weather=weather_desc,
        recommended_song=song
    )

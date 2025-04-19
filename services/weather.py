
import os
import httpx

OPENWEATHER_API_KEY = "da6163f063f576e63789fa39e6e36f40"

WEATHER_MOOD_MAP = {
    "Clear": "happy",
    "Clouds": "calm",
    "Rain": "sad",
    "Drizzle": "sad",
    "Thunderstorm": "angry",
    "Snow": "calm",
    "Mist": "neutral",
    "Fog": "neutral",
}

async def get_weather_mood(city: str):
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY not set")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url, params=params)
        r.raise_for_status()
        data = r.json()

    condition = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    mood = WEATHER_MOOD_MAP.get(condition, "neutral")
    return mood, description

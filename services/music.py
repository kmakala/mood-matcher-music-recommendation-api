
import os
import httpx

LASTFM_API_KEY = "fffaa918cb5a9bc9e6800531fa525c16"

async def get_song_for_mood(mood: str):
    if not LASTFM_API_KEY:
        raise RuntimeError("LASTFM_API_KEY not set")
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "tag.gettoptracks",
        "tag": mood.lower(),
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": 1,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url, params=params)
        r.raise_for_status()
        data = r.json()

    track = data["tracks"]["track"][0]
    return {
        "name": track["name"],
        "artist": track["artist"]["name"],
        "url": track["url"],
    }

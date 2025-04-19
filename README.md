
# Mood‑Weather Music Recommender

Small FastAPI micro‑service that checks if your mood matches the current weather in a city and suggests a fitting song.

## Quickstart
```bash
pip install -r requirements.txt
export OPENWEATHER_API_KEY=...
export LASTFM_API_KEY=...
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

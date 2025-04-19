
## 1. What's the idea? 🤔  
We're building a simple and fun **REST API** that does this:
1. You tell it how you're feeling (**your mood**) and where you are (**your city**).
2. It checks the **current weather** in your city.
3. It figures out if the weather fits your mood.
4. Based on all that, it gives you a **song recommendation** that matches your vibe!

---

## 2. What are we building it with? 🛠️

| Layer | Tool | Why this one? |
|-------|------|----------------|
| Web API | **FastAPI** | Super fast, easy to use, comes with Swagger docs automatically |
| Language | **Python 3.10+** | Clean syntax, async-friendly, great libraries |
| HTTP client | **httpx** | Plays nicely with FastAPI’s async nature |
| Testing | **pytest + pytest-asyncio** | Easy to write and read tests |
| Deployment | **requirements.txt + Dockerfile** | Makes setup and deployment simple |

---

## 3. How does it work? 🔧

Here’s the general flow of the app:

```
You (client) 
    │
    ▼
FastAPI app
    ├── Calls WeatherService (OpenWeatherMap)
    └── Calls MusicService (Last.fm)
         └── MoodMatcher: compares mood with weather
```

- **WeatherService**: Talks to OpenWeatherMap to get current weather.
- **MusicService**: Uses Last.fm to find songs based on mood tags.
- **MoodMatcher**: Connects weather vibes with mood vibes (e.g. “clear sky” = happy).

---

## 4. API Endpoints 🌐

| Method | URL | What You Send | What You Get Back |
|--------|-----|----------------|--------------------|
| GET | `/health` | – | `{"status": "ok"}` – just to check if it’s running |
| POST | `/recommend` | `{"city": "London", "mood": "happy"}` | You get a song suggestion! |

### Example Response:

```json
{
  "mood_match": true,
  "city_weather": "clear sky",
  "recommended_song": {
    "name": "Here Comes The Sun",
    "artist": "The Beatles",
    "url": "https://www.last.fm/music/The+Beatles/_/Here+Comes+the+Sun"
  }
}
```

---

## 5. Secrets & Config 🔐

To keep things safe, use environment variables:

| Variable | What It’s For |
|----------|----------------|
| `OPENWEATHER_API_KEY` | To access weather data |
| `LASTFM_API_KEY` | To access song data from Last.fm |

You can store these in a `.env` file or your cloud service's secret manager.

---

## 6. Handling Errors 🚨

We’re planning for common issues:

- **400** – If someone sends bad data (like an empty mood).
- **502** – If one of the APIs we depend on goes down.
- **429** – If we hit API rate limits.

---

## 7. How to Run It Locally 💻

Set up your virtual environment and start the app:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export OPENWEATHER_API_KEY=your_key_here
export LASTFM_API_KEY=your_other_key_here

uvicorn main:app --reload
```

---

## 8. Running Tests ✅

To check that everything works:

```bash
pytest
```

---

## 9. Postman Setup 🧪

If you're using Postman to test:

1. Import `postman_collection.json`
2. Set these variables:
   - `base_url` – like `http://127.0.0.1:8000`
   - `city`, `mood` – your input values

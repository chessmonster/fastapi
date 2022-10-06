# main.py

import requests
import json

from fastapi import FastAPI

app = FastAPI()

@app.get("/movie/{title}")
async def movie(title):
    api_key = "3f27c730"
    res = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={title}")
    return json.loads(res.content.decode('utf-8'))

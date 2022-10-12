# main.py

import requests
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    # maybe add here the IP of amplify app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movie/{title}")
async def movie(title):
    api_key = "3f27c730"
    res = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={title}")
    return json.loads(res.content.decode('utf-8'))

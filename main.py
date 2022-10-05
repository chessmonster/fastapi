# main.py

import requests
import json

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/hmm")
async def hmm():
    return {"hmmm":"hmmmmmm"}

@app.get("/movie/{title}")
async def movie(title):
    api_key = "3f27c730"
    res = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={title}")
    return json.loads(res.content.decode('utf-8'))

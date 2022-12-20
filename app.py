from fastapi import FastAPI
from pydantic import BaseModel

from src.summarizer import summarize

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/summarize")
async def annotate(item: Item):
    return summarize(item.text)
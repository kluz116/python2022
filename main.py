from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    isOffer:Optional[bool] = None


@app.get("/")
async def readroot():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def getItemID(item_id:int):
    return {"item_id":item_id}




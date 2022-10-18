from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    quantity: int

inventory = {
    0 : {"name": "item1", "quantity": 10},
    1 : {"name": "item2", "quantity": 20},
}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/inventory")
async def read_inventory():
    return inventory
    
@app.get("/inventory/{item_id}")
async def read_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]
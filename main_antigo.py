from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    quantity: int

gl_id = 1 
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

@app.post("/inventory")
async def create_item(item: Item):
    global gl_id
    gl_id += 1
    inventory[gl_id] = item
    return inventory

@app.put("/inventory/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item
    return inventory[item_id]

@app.delete("/inventory/{item_id}")
async def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    global gl_id
    gl_id -= 1
    del inventory[item_id]
    return {"message": "Item deleted successfully"}
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/inventory/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory_by_name(db, name=inventory.name)
    if db_inventory:
        raise HTTPException(status_code=400, detail="Inventory already registered")
    return crud.create_inventory(db=db, inventory=inventory)

@app.get("/inventory/", response_model=List[schemas.Inventory])
def get_all_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inventories = crud.get_all_inventory(db, skip=skip, limit=limit)
    return inventories
    

@app.get("/inventory/{inventory_id}", response_model=schemas.Inventory)
def get_inventory(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@app.delete("/inventory/{inventory_id}", response_model=schemas.Inventory)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.delete_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory



@app.post("/movement/", response_model=schemas.Movement)
def create_movement(movement: schemas.MovementCreate, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=movement.inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return crud.create_movement(db=db, movement=movement)

@app.get("/movement/", response_model=List[schemas.Movement])
def get_all_movement(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movements = crud.get_all_movement(db, skip=skip, limit=limit)
    return movements

@app.get("/movement/{movement_id}", response_model=schemas.Movement)
def get_movement(movement_id: int, db: Session = Depends(get_db)):
    db_movement = crud.get_movement(db, movement_id=movement_id)
    if db_movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return db_movement
    
@app.get("/inventory/movements/{inventory_id}", response_model=List[schemas.Movement])
def get_movement_by_inventory_id(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return crud.get_movement_by_inventory_id(db, inventory_id)

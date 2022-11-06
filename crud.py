from sqlalchemy.orm import Session

import models, schemas

# Todas as operações:
#     get all inventory
#     get inventory by inventory_id
#     post new inventory (quantity = 0)
#     delete a inventory by inventory_id
#     put a inventory (no callable on main, just by posting a movement)(call inside post movement crud)

#     get a movement by movement_id
#     get all movements
#     post a movement (call the put inventory method)


def get_all_inventory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Inventory).offset(skip).limit(limit).all()

def get_inventory(db: Session, inventory_id: int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()

def get_inventory_by_name(db: Session, name: str):
    return db.query(models.Inventory).filter(models.Inventory.name == name).first()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(name=inventory.name, quantity = 0)
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, inventory_id: int):
    db_inventory = get_inventory(db, inventory_id)
    db.delete(db_inventory)
    db.commit()
    return db_inventory

def edit_inventory_quantity(db: Session, inventory_id: int, new_quantity: int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).update({"quantity": new_quantity}, synchronize_session="fetch")



def get_all_movement(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movement).offset(skip).limit(limit).all()

def get_movement_by_inventory_id(db: Session, inventory_id: int):
    return db.query(models.Movement).filter(models.Movement.inventory_id == inventory_id).all()

def get_movement(db: Session, movement_id: int):
    return db.query(models.Movement).filter(models.Movement.id == movement_id).first()

def create_movement(db: Session, movement: schemas.MovementCreate):
    db_movement = models.Movement(inventory_id = movement.inventory_id, quantity_change = movement.quantity_change)
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)

    db_inventory = get_inventory(db, movement.inventory_id)
    new_quantity = db_inventory.quantity + movement.quantity_change
    if new_quantity < 0:
        new_quantity = 0
    edit_inventory_quantity(db, movement.inventory_id, new_quantity)
    db.commit()
    return db_movement
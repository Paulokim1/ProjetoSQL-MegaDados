from typing import List, Union

from pydantic import BaseModel

#Create an InventoryBase and MovementBase Pydantic models (or let's say "schemas") to have common attributes while creating or reading data.
#And create an InventoryCreate and MovementCreate that inherit from them (so they will have the same attributes), plus any additional data (attributes) needed for creation.

class InventoryBase(BaseModel):
    name: str


class MovementBase(BaseModel):
    inventory_id: int
    quantity_change: int

class InventoryCreate(InventoryBase):
    pass

class MovementCreate(MovementBase):
    pass

#Now create Pydantic models (schemas) that will be used when reading data, when returning it from the API.


class Inventory(InventoryBase):
    id: int
    quantity: int #Quando criamos um inventario, ele comeca em 0.
    #Não retorna todas as movimentações em um GET

    class Config:
        orm_mode = True

class Movement(MovementBase):
    id: int
    inventory: Inventory

    class Config:
        orm_mode = True
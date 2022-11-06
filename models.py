from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base #We will use this Base class we created before to create the SQLAlchemy models.
                           #SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database.

class Inventory (Base):
    __tablename__ = "inventory" #The __tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models.
    #We use Column from SQLAlchemy as the default value.
    #And we pass a SQLAlchemy class "type", as Integer, String, and Boolean, that defines the type in the database, as an argument.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    quantity = Column(Integer, index=True)

    movements = relationship("Movement", back_populates="inventory")

class Movement (Base):
    __tablename__ = "movement"
    #Falta colunas (?)
    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"))
    quantity_change = Column(Integer, index=True) #Positivo ou negativo 
    
    inventory = relationship("Inventory", back_populates="movements")

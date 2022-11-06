from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DB_PASS = os.environ.get("DB_PASS")
SQLALCHEMY_DATABASE_URL = f"mysql://root:{DB_PASS}@localhost:3306/projetoMegaDados"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Each instance of the SessionLocal class will be a database session. 
                                                                            #The class itself is not a database session yet.
                                                                            #But once we create an instance of the SessionLocal class, 
                                                                            #this instance will be the actual database session.

Base = declarative_base() #Now we will use the function declarative_base() that returns a class.
                          #Later we will inherit from this class to create each of the database models or classes (the ORM models)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# # default
# engine = create_engine("mysql://scott:tiger@localhost/foo")

# # mysqlclient (a maintained fork of MySQL-Python)
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")

# # PyMySQL
# engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")


# SQLALCHEMY_DATABASE_URL = "mysql://user:password@mysql/db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Each instance of the SessionLocal class will be a database session. 
                                                                            #The class itself is not a database session yet.
                                                                            #But once we create an instance of the SessionLocal class, 
                                                                            #this instance will be the actual database session.

Base = declarative_base() #Now we will use the function declarative_base() that returns a class.
                          #Later we will inherit from this class to create each of the database models or classes (the ORM models)
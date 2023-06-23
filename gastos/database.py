from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from databases import Database

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:ojodehorus.42@localhost/expenses_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
database = Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

def connect_to_database():
    database.connect()

def disconnect_from_database():
    database.disconnect()

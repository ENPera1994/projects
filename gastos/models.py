import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))

class User(BaseModel):
    id: int
    name: str
    email: str

class Category(BaseModel):
    id: int
    name: str

class Expense(BaseModel):
    id: int
    title: str
    amount: float
    day: datetime.date
    category_id: int
    user_id: int

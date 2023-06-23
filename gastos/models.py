import datetime
from pydantic import BaseModel

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

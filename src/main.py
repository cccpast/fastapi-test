from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

class Student(BaseModel):
  name: str
  age: int
  gender: Union[str, None] = None
  address: Union[str, None] = None

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello, fastapi!!"}

# ex) http://127.0.0.1:8000/items/2?q=hogehoge
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.post("/students/")
async def create_item(student: Student):
  return student
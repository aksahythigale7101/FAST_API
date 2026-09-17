from logging import info

from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
app = FastAPI()


class student(BaseModel):
    name: str
    age: int
    email: str

# @app.get("/info/")
# def read_root()->student:
#     return {"name": "akshay", "age":29,"email":"akshay@gmail.com"}

# @app.get("/info/")
# def read_root()->List[student]:
#     return [{"name": "akshay", "age":29,"email":"akshay@gmail.com"}
#             ,{"name": "pranjal", "age":28,"email":"ppp#gmail.com"},
#             {"name": "aanandi", "age":6,"email":"aandi@gmail.com"},]
#



class UserIn(BaseModel):
    username: str
    user_id: int

class Userout(UserIn):
    passward:str


@app.get("/info")
def read_root(user:Userout)->UserIn:
    return user







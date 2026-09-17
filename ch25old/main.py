from logging import info

from pydantic import BaseModel
from fastapi import FastAPI
from typing import List, Any

app = FastAPI()


class Proudct(BaseModel):
    name: str
    age: int
    email: str

class Productout(BaseModel):
    passward:str

#witout respomce model paramter
# @app.get("/info/")
# def read_root()->student:
#     return {"name": "akshay", "age":29,"email":"akshay@gmail.com"}

#with respomce model paramter
@app.get("/info/",response_model=Proudct)
def read_root():
    return {"name": "akshay", "age":29,"email":"akshay@gmail.com"}
    #return {"Hello": "World"} #--get error cause reponce model is used


@app.post("/proudcts/",response_model=Proudct)
def read_root1(pro: Proudct):
    #return {"name": "akshay", "age":29,"email":"akshay@gmail.com"}
    #return {"Hello": "World"} #--get error cause reponce model is used
    return pro


class UserIn(BaseModel):
    username: str
    user_id: int

class Userout(UserIn):
    passward:str


# @app.post("/info/",response_model=UserIn)
# def read_root19(user:Userout):
#     return user

#
# @app.post("/info/",response_model=UserIn)
# def read_data(user:Userout)->Any:
#     return user

@app.post("/info/",response_model=None)#siable
def read_info(user:Userout)->Any:
    return user



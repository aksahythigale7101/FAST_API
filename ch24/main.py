

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Proudct(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProudctOut(BaseModel):
    name: str
    price: float
    
    

# Without Return type
# @app.get("/proudcts/")
# async def get_proudct():
#     return {"Status": "OK !"}


# with return type annoution
# @app.get("/proudcts/")
# async def get_proudct() -> Proudct:
#     return {"id":1,"name":"Moto G7","price":2500.55,"stock":5}


# optional and extra feild add
# @app.get("/proudcts/")
# async def get_proudct() -> Proudct:
#     return {"id":1,"name":"Moto G7","price":2500.55}
#     #return {"id":1,"name":"Moto G7","price":2500.55,"color":"black"}


#List
# @app.get("/proudcts/")
# async def create_proudct() -> List[Proudct]:
#     return [
#             {"id":1,"name":"Moto G7","price":2500.55,"stock":5},
#             {"id":2,"name":"iphone 17","price":6000.75,"stock":7},
#             {"id":3,"name":"redami","price":1500.99,"stock":6}
#             ]


#post
# data as input and return in class
# @app.post("/proudcts/")
# async def get_proudct(proudct:Proudct)->Proudct:
#     return proudct

# diff return type
@app.post("/proudcts/")
async def create_proudct(proudct:Proudct)->ProudctOut:
    return proudct

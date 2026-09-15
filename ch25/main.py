
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional

app = FastAPI()


class Proudct(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None


class ProudctOut(BaseModel):
    name: str
    price: float


# without responce model paratmater
# @app.get("/proudcts/")
# async def get_proudct() -> Proudct:
#     return {"id":1,"name":"Moto G7","price":2500.55,"stock":5}

# with responce model paramter
# @app.get("/proudcts/", response_model=Proudct)
# async def get_proudct():
#     return {"id":10,"name":"Moto G7","price":2500.55,"stock":5}


# with LIST responce model paramter
# @app.get("/proudcts/", response_model=List[Proudct])
# async def get_proudct():
#     return [
#         {"id": 1, "name": "Moto G7", "price": 2500.55, "stock": 5},
#         {"id": 2, "name": "iphone 17", "price": 6000.75, "stock": 7},
#         {"id": 3, "name": "redami", "price": 1500.99, "stock": 6},
#     ]


# with responce model paramter
# @app.post("/proudcts/", response_model=Proudct)
# async def create_proudct(proudct: Proudct):
#     return proudct


# using responce model with diff in or diff output
# @app.post("/proudcts/", response_model=ProudctOut)
# async def create_proudct(proudct: Proudct):
#     return proudct


# @app.post("/proudcts/", response_model=ProudctOut)
# async def create_proudct(proudct: Proudct)->Any:
#     return proudct


# @app.post("/proudcts/", response_model=None)
# async def create_proudct(proudct: Proudct):
#     return proudct

StudeInfo = [
    {
        "name": "Amit Sharma",
        "age": 28,
        "gender": "Male",
        "email": "amit.sharma@example.com",
        "DeptID": 1,
    },
    {
        "name": "Priya Singh",
        "age": 25,
        "gender": "Female",
        "email": "priya.singh@example.com",
        "DeptID": 2,
    },
    {
        "name": "Rahul Verma",
        "age": 32,
        "gender": "Male",
        "email": "rahul.verma@example.com",
        "DeptID": 1,
    },
    {
        "name": "Sneha Patil",
        "age": 29,
        "gender": "Female",
        "email": "sneha.patil@example.com",
        "DeptID": 3,
    },
    {
        "name": "Vikram Joshi",
        "age": 35,
        "gender": "Male",
        "email": "vikram.joshi@example.com",
        "DeptID": 2,
    }
]


class Student(BaseModel):
    name: str
    age: int
    gender: str
    email: Optional[str] = None
    DeptID: int


# @app.get("/students/{Sname}", response_model=Student,response_model_exclude_unset=True)
# async def create_info(Sname: str):

#     for student in StudeInfo:
#         if student["name"] == Sname:
#             return student
#     raise HTTPException(
#         status_code=404,
#         detail="Student not found"
#     )
@app.get("/students/{Sname}", response_model=Student, response_model_include="email")
async def create_info(Sname: str):

    for student in StudeInfo:
        if student["name"] == Sname:
            return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
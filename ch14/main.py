from typing import Annotated

from pydantic import AfterValidator

from fastapi import FastAPI, Query,Path
from pydantic_extra_types import path

app = FastAPI()

PROUDCT = [
    {
        "name": "Amit Sharma",
        "age": 28,
        "gender": "Male",
        "email": "amit.sharma@example.com",
        "DeptID": 1
    },
    {
        "name": "Priya Singh",
        "age": 25,
        "gender": "Female",
        "email": "priya.singh@example.com",
        "DeptID": 2
    },
    {
        "name": "Rahul Verma",
        "age": 32,
        "gender": "Male",
        "email": "rahul.verma@example.com",
        "DeptID": 1
    },
    {
        "name": "Sneha Patil",
        "age": 29,
        "gender": "Female",
        "email": "sneha.patil@example.com",
        "DeptID": 3
    }
]


#Numeric valdiation
# @app.get("/proudct/{p_age}")
# async def get_proudct(p_age: Annotated[int, Path(ge=18,le=55)]):
#
#     filterProudct = []
#
#     for proudct in PROUDCT:
#         if proudct["age"] == p_age:
#             filterProudct.append(proudct)
#
#     if filterProudct:
#         return filterProudct
#
#     return "Data Not found"




#auery and path prameter
@app.get("/proudct/{p_age}")
async def get_proudct(p_age: Annotated[int, Path(ge=18,le=55)],
                      serch: str | None = Query(default=None,max_length=5)):

    filterProudct = []

    for proudct in PROUDCT:
        if proudct["age"] == p_age or   proudct["name"] == str:
            filterProudct.append(proudct)

    if filterProudct:
        return filterProudct

    return "Data Not found"



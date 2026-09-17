from typing import Annotated

from pydantic import AfterValidator

from fastapi import FastAPI, Query

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
    },
    {
        "name": "Vikram Joshi",
        "age": 35,
        "gender": "Male",
        "email": "vikram.joshi@example.com",
        "DeptID": 2
    },
    {
        "name": "Anjali Deshmukh",
        "age": 27,
        "gender": "Female",
        "email": "anjali.d@example.com",
        "DeptID": 1
    },
    {
        "name": "Rohan Kulkarni",
        "age": 31,
        "gender": "Male",
        "email": "rohan.k@example.com",
        "DeptID": 4
    },
    {
        "name": "Neha Gupta",
        "age": 26,
        "gender": "Female",
        "email": "neha.gupta@example.com",
        "DeptID": 3
    },
    {
        "name": "Suresh Nair",
        "age": 40,
        "gender": "Male",
        "email": "suresh.nair@example.com",
        "DeptID": 2
    },
    {
        "name": "Pooja Reddy",
        "age": 24,
        "gender": "Female",
        "email": "pooja.reddy@example.com",
        "DeptID": 1
    },
    {
        "name": "Karan Mehta",
        "age": 33,
        "gender": "Male",
        "email": "karan.mehta@example.com",
        "DeptID": 4
    },
    {
        "name": "Divya Iyer",
        "age": 30,
        "gender": "Female",
        "email": "divya.iyer@example.com",
        "DeptID": 3
    },
    {
        "name": "Arjun Rao",
        "age": 36,
        "gender": "Male",
        "email": "arjun.rao@example.com",
        "DeptID": 2
    },
    {
        "name": "Kavita Pillai",
        "age": 38,
        "gender": "Female",
        "email": "kavita.p@example.com",
        "DeptID": 1
    },
    {
        "name": "Manish Yadav",
        "age": 34,
        "gender": "Male",
        "email": "manish.yadav@example.com",
        "DeptID": 4
    },
    {
        "name": "Naru Modi",
        "age": 75,
        "gender": "Male",
        "email": "naru.m@example.com",
        "DeptID": 5
    }
]

filterProudct = []


# # using query paramer get proudct
# @app.get("/proudct")
# async def get_proudct(serch: str | None = None):
#
#     for proudct in PROUDCT:
#         if proudct["name"] == serch:
#             filterProudct.append(proudct)
#             return filterProudct
#         #else:
#            # return ("Data Not found ", filterProudct)
#
#     return PROUDCT

# # using query paramer get proudct in validaiton
# @app.get("/proudct")
# async def get_proudct(serch: str | None = Query(default=None,max_length=5)):
#
#     for proudct in PROUDCT:
#         if proudct["name"] == serch:
#             filterProudct.append(proudct)
#             return filterProudct
#         #else:
#            # return ("Data Not found ", filterProudct)
#
#     return PROUDCT

# using query single parameter get proudct in validaiton in annoted
# @app.get("/proudct")
# async def get_proudct(serch:Annotated[ str | None ,Query(max_length=15,min_length=2)]=None):
#
#     for proudct in PROUDCT:
#         if proudct["name"] == serch:
#             filterProudct.append(proudct)
#             return filterProudct
#         #else:
#            # return ("Data Not found ", filterProudct)
#
#     return PROUDCT
#

# #using query List parameter get proudct in validaiton in annoted
# @app.get("/product")
# async def get_proudct(serch: Annotated[list[str] | None, Query(alias=q)] = None):
#    #if serch:
#         for product in PROUDCT:
#
#             if product["name"] in  serch:
#                 filterProudct.append(product)
#             return filterProudct
#             # else:
#             # return ("Data Not found ", filterProudct)
#
#         return PROUDCT



#custom validation
def chechk_valid_id(id:str):
    if not id.startswith("prod-"):
        raise ValueError("Invalid proudct ID AND MUST START WITH 'prod-'")
    return id






@app.get("/proudct")
async def get_proudct(id :Annotated[ str | None,AfterValidator(chechk_valid_id)]=None):
   if id:
       return {"id is correct " : id}
   else:
       return {"id is incorrect ", id}



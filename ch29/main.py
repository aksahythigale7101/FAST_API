from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()


student = {
    "Amit Sharma": "amit.sharma@example.com",
    "Priya Singh": "priya.singh@example.com",
    "Sneha Patil": "sneha.patil@example.com",
}

# @app.get("/info/{name}")
# async def Get_User(name:str):
#     if name not in student:
#         raise HTTPException(status_code=404,detail="Student is not found")
#     return student[name]


# Heder data added
# @app.get("/info/{name}")
# async def Get_User(name:str):
#     if name not in student:
#         raise HTTPException(status_code=404,detail="Student is not found",headers={"x-error-type":"missing items"})
#     return student[name]


#Custom Exceaptions
class ProductNotFoundException(Exception):

    def __init__(self, product_id: int):
        self.product_id = product_id


@app.exception_handler(ProductNotFoundException)
async def product_not_found_handler(
    request: Request,
    exc: ProductNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": "Product not found",
            "product_id": exc.product_id
        }
    )


@app.get("/product/{product_id}")
async def get_product(product_id: int):

    if product_id != 1:
        raise ProductNotFoundException(product_id)

    return {
        "id": 1,
        "name": "Laptop"
    }


# override default exceapction handler--------------------------
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(
#     request: Request,
#     exc: RequestValidationError
# ):
#     return JSONResponse(
#         status_code=400,
#         content={
#             "success": False,
#             "message": "Invalid request data",
#             "errors": exc.errors()
#         }
#     )

# #override default exceapction handler
# @app.get("/product/{product_id}")
# async def get_product(product_id: int):
#     return {
#         "id": product_id
#     }
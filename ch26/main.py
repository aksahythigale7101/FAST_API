from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()


# Without FROM using 
# class LoginRequest(BaseModel):
#     username: str
#     password: str

# @app.post("/login")
# def login(data: LoginRequest):
#     return {
#         "username": data.username,
#         "password": data.password
#     }



#  with FROM used means HTML code in FORM feild
# @app.post("/login")
# async def login(
#     username: str = Form(),
#     password: str = Form()
# ):
#     return {
#         "username": username,
#         "password": password
#     }


# using  FROM Handle with annotaions
# @app.post("/register")
# async def register(
#     username: Annotated[str, Form(min_length=3, max_length=20)],
#     age: Annotated[int, Form(ge=18, le=60)]
# ):
#     return {
#         "username": username,
#         "age": age
#     }




# @app.post("/user")
# async def create_user(
#     username: Annotated[str, Form()],
#     email: Annotated[str | None, Form()] = None
# ):
#     return {
#         "username": username,
#         "email": email
#     }



@app.post("/register")
async def register(
    name: Annotated[str, Form(min_length=3)],
    email: Annotated[str, Form()],
    age: Annotated[int, Form(ge=18)]
):
    return {
        "message": "Registration successful",
        "name": name,
        "email": email,
        "age": age
    }
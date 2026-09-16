
from fastapi import FastAPI, Form
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()

# using pydentic model
# class CarInfo(BaseModel):
#     Model: str
#     CC: int
#     Colour: str


# using pydantic model with validaion
class CarInfo(BaseModel):
    Model: str = Field(min_length=2, max_length=10)
    CC: int = Field(gt=0, le=9999) 
    Colour: str = Field(min_length=2, max_length=10)



@app.post("/car/")
async def catDisplay(data: Annotated[CarInfo, Form()]):
    return data

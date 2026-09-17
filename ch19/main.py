from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# using Feild Level examples
class Proudct(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["ABC"])
    email: str | None = Field(default=None, examples=["abc@gmail.com"])
    price: float = Field(examples=[1.5])


@app.post("/proudct")
async def Roots(proudct: Proudct):
    return {"proudct": proudct}


# using pyandic json_schema_)extrea


class Brands(BaseModel):
    id: int
    model: str
    color: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "model": "M5",
                    "color": "#ff0000",

                }
            ]

        }
    }
@app.post("/proudct1")
async def Roots1(proudct1: Brands):
    return {"proudct": proudct1}

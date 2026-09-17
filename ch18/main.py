from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# Nested models
class Category(BaseModel):
    name: str = Field(
        title="Thiame",
        description="Tame",
        max_length=50,
        min_length=1
    )
    description: str | None = Field(
        default=None,
        title="This is categoery description",
        description="This is categoery description",
        max_length=500,

    )


# model wich used submodel
class Proudct(BaseModel):
    name: str = Field(
        title="Proudct Name",
        pattern="^[A-Za-z0-9 ]+$",
        min_length=300,
        max_length=1,
    )
    price: float = Field(
        default=0,
        ge=2,
        title="Proudct Price",
        max_digits=2,
        description="Proudct Price it to high",
    )

    # category: Category | None = Field(
    #     default=None,
    #     title="Proudct Category",
    #     description="Proudct Category",
    # )
    # attribute with same submodels using list
    category: list[Category] | None = Field(

        default=None,
        title="PCattt",
        description="Proudct Category"
    )


@app.post("/proudct")
async def createroot(proudct: Proudct):
    return proudct



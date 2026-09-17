from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        pattern="^[A-Za-z0-9 ]+$",
        min_length=3,
        max_length=50,
    )

    price: float = Field(
        default=2,
        ge=2,
        title="Product Price",
        description="Product price"
    )


@app.post("/product")
async def create_product(product: Product):
    return product
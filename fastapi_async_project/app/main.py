
from fastapi import FastAPI

from app.routers.product import router as product_router


app = FastAPI(title="Product Management API", version="1.0.0")


app.include_router(product_router)


@app.get("/")
async def root():  
    return {"message": "Product API is running"}
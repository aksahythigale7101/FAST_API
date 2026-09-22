import time
import uuid
from fastapi import FastAPI

from app.routers.product import router as product_router
from app.middleware.custom_middleware import *
from app.middleware.cors import setup_cors
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Product Management API", version="1.0.0")

# Middleware
app.add_middleware(
    CORSMiddleware,

    allow_origins=["http://localhost:5173"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# Router
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Product API is running"}

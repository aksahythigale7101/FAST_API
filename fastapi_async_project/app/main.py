import time
import uuid
from fastapi import FastAPI

from app.routers.product import router as product_router
from app.middleware.custom_middleware import *
from app.middleware.cors import setup_cors
app = FastAPI(title="Product Management API", version="1.0.0")

# Middleware
app.middleware("http")(request_id_middleware)
app.middleware("http")(logging_middleware)
setup_cors(app)






# Router
app.include_router(product_router)


@app.get("/")
async def root():  
    return {"message": "Product API is running"}
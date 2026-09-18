from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services import product as product_service


router = APIRouter(prefix="/products", tags=["Products"])


DbSession = Annotated[AsyncSession, Depends(get_db)]


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreate, db: DbSession):
    return await product_service.create_product(db, product_data)


@router.get("/", response_model=list[ProductResponse])
async def get_products(db: DbSession):
    return await product_service.get_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: DbSession):

    product = await product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_data: ProductUpdate, db: DbSession):

    product = await product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return await product_service.update_product(db, product, product_data)


@router.patch("/{product_id}", response_model=ProductResponse)
async def patch_product(product_id: int, product_data: ProductUpdate, db: DbSession):

    product = await product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return await product_service.update_product(db, product, product_data)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: DbSession):

    product = await product_service.get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await product_service.delete_product(db, product)

    return None
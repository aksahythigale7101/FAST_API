
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse


async def create_product(db: AsyncSession, product_data: ProductCreate):
    product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        quantity=product_data.quantity,
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)

    return product


async def get_products(db: AsyncSession):
    result = await db.execute(select(Product))
    product = result.scalars().all()
    return product


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalars().first()
    return product


async def update_product(
    db: AsyncSession, product: Product, product_data: ProductUpdate
):
    update_data = product_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(db: AsyncSession, product: Product):
    await db.delete(product)
    await db.commit()

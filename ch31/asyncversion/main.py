
import asyncio

from ch31.asyncversion.db import engine, AsyncSessionLocal
from  ch31.asyncversion.models import Base, User
from sqlalchemy import select


async def mainfile():

    # Create table
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    # Create user
    async with AsyncSessionLocal() as session:

        user = User(name="Harsh")

        session.add(user)

        await session.commit()

        await session.refresh(user)

        print("User created:", user.id)

    # Read users
    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(User)
        )

        users = result.scalars().all()

        for user in users:
            print(user.id, user.name)



# if __name__ == "__main__":
#     asyncio.run(mainfile())

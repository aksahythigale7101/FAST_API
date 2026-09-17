
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


# import sys
# print("PYTHON EXE:", sys.executable)

# try:
#     import aiosqlite
#     print("aiosqlite FOUND at:", aiosqlite.__file__)
# except ImportError:
#     print("aiosqlite NOT FOUND in this interpreter")


DATABASE_URL = "sqlite+aiosqlite:///async.db"

engine = create_async_engine(
    DATABASE_URL,
   
)# echo=True

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
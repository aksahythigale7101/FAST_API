import os
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

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one folder up = ch31
BASE_DIR = os.path.dirname(CURRENT_DIR)

# Create database file inside ch31
DB_PATH = os.path.join(BASE_DIR, "async.db")
print(DB_PATH)

DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"

engine = create_async_engine(DATABASE_URL)# echo=True


#DATABASE_URL = "sqlite+aiosqlite:///async.db"

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
from fastapi import FastAPI
from app.db.database import create_db_and_tables
from app.routers.auth import router as auth_router

app = FastAPI(title="FASTAPI Auth System")


@app.on_event("startup")
def startup():
    create_db_and_tables()


app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Authentication API"
    }

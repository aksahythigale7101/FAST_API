from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_Session
from app.schemas.user import UserCreate, UserResponse

from app.services.auth_service import login_user, register_user
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.token import TokenResponce

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, session: Annotated[Session, Depends(get_Session)]):
    try:
        user = register_user(session, user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login", response_model=TokenResponce, status_code=status.HTTP_200_OK)
def login(
    from_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_Session)],
):
    try:
        access_token = login_user(session, from_data.username, from_data.password)
        return {"access_token": access_token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


import secrets

current_user = {
    "id": 10,
    "name": "Akshay"
}
@router.post("/api-keys",tags=["temp"])
async def create_api_key(current_user:dict):

    api_key = secrets.token_urlsafe(32)

    return {"user_id": current_user["id"], "api_key": api_key}
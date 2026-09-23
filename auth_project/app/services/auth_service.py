from fastapi import HTTPException  # ✅ correct
from sqlmodel import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password
)
from app.repositories.user_repository import (get_user_by_username,
                                              get_user_by_email,
                                              create_user
                                              )


def register_user(session: Session, user_data: UserCreate):
    existing_username = get_user_by_username(session, user_data.username)

    if existing_username:
        raise HTTPException(status_code=400, detail="User with that username already exists")

    existing_email = get_user_by_email(session, user_data.email)

    if existing_email:
        raise HTTPException(status_code=400, detail="Email alredy exists")

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        role="user",
        is_active=True
    )
    return create_user(session, user)


def login_user(session: Session, usernmae: str, passward: str):
    user = get_user_by_username(session, usernmae)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username ")
    if not verify_password(passward, user.hashed_password):

        raise HTTPException(status_code=400, detail="Incorrect  password")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token = create_access_token(user_id=user.id, role=user.role)

    return access_token

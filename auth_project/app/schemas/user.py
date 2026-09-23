from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)

    email: EmailStr

    password: str = Field(min_length=8, max_length=50)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    role: str
    is_active: bool

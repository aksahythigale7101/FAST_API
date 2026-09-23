from pydantic import BaseModel


class TokenResponce(BaseModel):
    access_token: str
    token_type: str

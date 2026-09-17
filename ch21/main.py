from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

from typing import Annotated
class CookieData(BaseModel):
    model_config={"extra": "forbid"}#extra="forbid" means Pydantic rejects any extra field that is not defined inside the mode
    session_id: str
    user_id: int
    theme: str


@app.get("/proudct/recommendations")
async def recommendations(

    session_id: str | None = Cookie(default=None),
    user_id: int | None = Cookie(default=None),
    theme: str | None = Cookie(default=None)
):
    cookies = CookieData(
        session_id=session_id,
        user_id=user_id,
        theme=theme
    )

    return cookies

#extra="forbid" means Pydantic rejects any extra field that is not defined inside the model.
#curl -H "Cookie: session_id=12345 user_id=101; theme=dark" http://127.0.0.1:8000/proudct/recommendations
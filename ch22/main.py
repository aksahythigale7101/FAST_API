from multiprocessing.reduction import duplicate

from pydantic import BaseModel
from fastapi import FastAPI,Header
from typing import Annotated

app = FastAPI()

# @app.get("/proudct")
# async def root(user_agent:Annotated[None,Header()]):
#     return {"user_agent":user_agent}


#Handling duplicates heder
@app.get("/proudct")
async def root(
    x_token: Annotated[list[str] | None, Header()] = None
):
    return {"x_token": x_token}

#cmd
#curl -H "X-Token: foo" -H "X-Token: bar" http://127.0.0.1:8000/proudct

#foo and bar is duplicate tokemn
from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class HeaderData(BaseModel):
    model_config = {
        "extra": "forbid"}
    user_agent: str
    x_token: list[str] | None = None


@app.get("/product")
async def root(
    headers: Annotated[HeaderData, Header()]
):
    return headers


#curl -H "User-Agent: Mozilla/5.0" -H "X-Token: foo" -H "X-Token: bar" http://127.0.0.1:8000/product
#curl -H "User-Agent: spiderman" -H "X-Token: aa" -H "X-Token: bb" -H "X-Token: cc" http://127.0.0.1:8000/product

#witout forbidden extra value put in cmd so it igonre when forbidden
#and extra valeu added in cmd it gives error
'''
Error
{"detail":[{"type":"extra_forbidden","loc":["header","host"],"msg":"Extra inputs are not permitted","input":"127.0.0.1:8000"},{"type":"extra_forbidden","loc":["header","accept"],"msg":"Extra inputs are not permitted","input":"*/*"},{"type":"extra_forbidden","loc":["header","hed"],"msg":"Extra inputs are not permitted","input":"123"}]}
C:\>
'''

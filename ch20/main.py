from pydantic import BaseModel
from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()



#Cookie pareamter

@app.get("/proudct/recommendations")
async def get_recommendations(session_id:Annotated[str|None,Cookie()]=None):
    if session_id:
        return {"message":session_id ,"recodmendatione session id" : session_id}

    return {"message":"No session id is proviede,showing default recommendateions"}


#fastapi run--cmd--
#curl -H "Cookie: session_id=12345" http://127.0.0.1:8000/proudct/recommendations

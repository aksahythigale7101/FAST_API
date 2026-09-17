from dns import node
from fastapi import FastAPI

app = FastAPI()

#single paramanter

#single Query paramter
#@app.get("/root")
#async def singleroot(category: str):
   # return {"Status:": "OK ", " category": category}

#multiple query paramter
@app.get("/root")
async def multipleroot(category:str, limit:int):
    return {"Status:" : "OK ", " category":category , " limit ":limit}


#defult query paramter
@app.get("/root1")
async def multipleroot(category:str,  limit:int=10):
    return {"Status:" : "OK ", " category":category , " limit ":limit}

#optional query paramter
@app.get("/root2")
async def optionaleroot(category:str|None=None,  limit:int=10):
    return {"Status:" : "OK ", " category":category , " limit ":limit}


#path and query paramter
@app.get("/root3/{year}")
async def root(year:str,  limit:int=10):
    return {"Status:" : "OK ", " Year":year , " limit ":limit}


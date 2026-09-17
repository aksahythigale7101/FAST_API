
from fastapi import  FastAPI,Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()



class Proudct(BaseModel):
    id: int
    name: str
    age: int

class Seller(BaseModel):
    user :str
    mode:str |None

# mulitple body paremter pass
# @app.post("/proudct")
# async def Roots(proudct_data:Proudct,seller_data:Seller):
#     return {"proudcr":proudct_data,"seller":seller_data}

# #make body opetional
# @app.post("/proudct")
# async def Roots(proudct_data:Proudct,seller_data:Seller|None=None):
#     return {"proudcr":proudct_data,"seller":seller_data }



# #singular value body
# @app.post("/proudct")
# async def Roots(pData:Proudct,seller_data:Seller,sec_key:Annotated[str,Body()]):
#     return {"proudct":pData,"seller":seller_data }



#Embeded single paremater body
#without embed
# @app.post("/proudct")
# async def Roots(proudct:Proudct):
#     return {"proudcr":proudct}


#Embeded single paremater body
#with embed
@app.post("/proudct")
async def Roots(proudct:Annotated[Proudct,Body(embed=True)]):
    return {"proudcr":proudct}



from fastapi import  FastAPI

from pydantic import BaseModel

app = FastAPI()


class Proudct(BaseModel):
    id: int
    Brand: str | None
    Model: str
    color: str
    prize: int | None







# @app.post("/proudct")
# async def get_proudct(proudct_data:Proudct):
#     return proudct_data


# #access attribute inseide the function
# @app.post("/proudct")
# async def get_proudct(proudct_data:Proudct):
#     print(proudct_data.id)
#     print(proudct_data.Brand)
#     print(proudct_data.Model)
#     print(proudct_data.color)
#     return proudct_data
#
#



# #add new calcaulte attribute
# @app.post("/proudct")
# async def get_proudct(proudct_data:Proudct):
#     p_data=proudct_data.model_dump()
#     proudct_prize=proudct_data.prize+(proudct_data.prize*18/100)
#     p_data.update({"prize_tax":proudct_prize})
#
#     return p_data

# #combine body request with paramter

# @app.put("/proudct/{pID}")
# async def update_proudct(pID:int, proudct_data:Proudct):
#      return {"proudctId ": pID , " proudcta_data ": proudct_data}



#Adding query paramter
@app.put("/proudct/{pID}")
async def update_proudct(pID:int, proudct_data:Proudct,dicount:float|None=None):
     return {"proudctId ": pID , " proudcta_data ": proudct_data,"Dicount": dicount}




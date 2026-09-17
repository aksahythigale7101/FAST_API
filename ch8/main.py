from enum import Enum

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class proudctSorting(str,Enum):
       data="Data"
       bike="Bike"
       car="Car"


@app.get("/proudct/{_proudct}")
async def root(_proudct: proudctSorting):
      if(proudctSorting.data==_proudct):
        return {"message": "This my data"," sorting": _proudct}
      elif(proudctSorting.bike==_proudct):
          return {"message": "This my motorcycle "," sorting": _proudct}
      elif(proudctSorting.car==_proudct):
          return {"message": "This my car "," sorting": _proudct}
      else:
          return {"message": "Not Match Enum "," sorting": _proudct}





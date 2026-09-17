from fastapi import FastAPI

app = FastAPI()

#read or fetch all data
@app.get("/proudct")
async def all_proudct():
 return ("responce: This is proudct!!")

#read single data
@app.get("/proudct/{proudct_id}")
async def all_proudcts(proudct_id: int):
 return (f"responce: This is proudctId :{proudct_id}")


#read post create and insert data
@app.post("/proudct}")
async def insert_proudct(new_proudct: dict):
 return (f"responce: This is Created  :  {new_proudct}")


#read put update data
@app.put("/proudct/{proudct_id}")
async def update_proudct(new_proudct: dict, proudct_id: int):
 return (f"responce: This is Created New  ProuctID : {proudct_id} And"
         f"This is a new data : {new_proudct}")

#read patch proudct data
@app.patch("/proudct/{proudct_id}")
async def patch_proudct(new_proudct: dict, proudct_id: int):
 return (f"responce: This is Created New  ProuctID : {proudct_id} And"
         f"This is a new data : {new_proudct}" )

#read single data
@app.delete("/proudct/{proudct_id}")
async def Delete_proudcts(proudct_id: int):
 return (f"responce: Delete Data , This is proudctId :{proudct_id}")


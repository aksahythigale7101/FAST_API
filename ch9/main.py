from fastapi import FastAPI

app = FastAPI()


#read single data
@app.get("/pro/{proudct_name:path}")
async def all_proudcts(proudct_name: str):
 return (f"responce: This is proudctId :{proudct_name}")

from fastapi import FastAPI,status
app = FastAPI()

#multiple query paramter
@app.get("/root",status_code=status.HTTP_200_OK)
async def multipleroot():
    return {"Status:" : "OK "}


from fastapi import FastAPI

app = FastAPI()


# proudct type int checkking
@app.get("/proudct/{p_id}")
async def int_proudct(p_id: int):
    return {"p_id ": p_id}


# proudct type string checking
@app.get("/proudct1/{p_title}")
async def str_proudct(p_title: str):
    return {" This is titale ", p_title}

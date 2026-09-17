from fastapi import FastAPI

app = FastAPI()

# Check orders
@app.get("/proudct/999")
async def number_root():
    return {"999 number data fetch"}

@app.get("/proudct/{p_title}")
async def number_root_str(p_title: str):
    return {"responce:title data fetch",
            "actual data", p_title}








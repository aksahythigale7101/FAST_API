from  fastapi import FastAPI

app=FastAPI()# this is fast api object


@app.get("/")
def home():
    return {"message":"This is my First FastAPI Project!! "}




#Run File
#fastapi run
#fastapi dev main.py
#uvicorn main:app --reload
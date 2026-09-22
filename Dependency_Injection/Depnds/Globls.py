from fastapi import FastAPI, Depends

def check_auth():
    print("Authentication checked")


app = FastAPI(
    dependencies=[
        Depends(check_auth)
    ]
)


@app.get("/products")
def products():
    return {"message": "Products"}


@app.get("/users")
def users():
    return {"message": "Users"}


@app.get("/orders")
def orders():
    return {"message": "Orders"}


from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def get_message():
    print(" HELLO AKSHAY ")
    return(" HELLO AKSHAY ")

# @app.get("/")
# def home(message: str = Depends(get_message)):
#     return message


def user_info():
    return {"Name": "Akshay", "ID": 10}


# @app.get("/")
# def home(message: dict = Depends(user_info)):
#     return message


#   Dependency can accept parameters


# def get_token(x_token: str = Header()):
#     return x_token


# @app.get("/profile")
# def home(tokens: str = Depends(get_token)):
#     return {"tokenX": tokens}


#  Dependency Injection with Authentication


def check_user(authorization: str = Header()):
    if authorization != "Bearer abc":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"Name": "Akshay", "ID": 10, "Ph": 9766656993}


# @app.get("/profile")
# def users(tokens: str = Depends(check_user)):
#     return {"tokenX": tokens}


#  Dependency chaining


def get_token(x_token: str = Header()):
    return x_token


def get_users(x_token: str = Depends(get_token)):
    return {"x_token": x_token, "user": "Akshay"}


@app.get("/profile")
def profile(user=Depends(get_users)):
    return user


#  Dependency with multiple dependencies


@app.get("/Dashboard")
def profile(user=Depends(get_message), userinfo=Depends(user_info)):
    return {"User": user, "UserInfo": userinfo}




#  Class as Dependency


class ProductFilters:

    def __init__(
        self,
        search: str | None = None,
        category: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None
    ):
        self.search = search
        self.category = category
        self.min_price = min_price
        self.max_price = max_price



@app.get("/filtes")
def profile(filter:ProductFilters=Depends(ProductFilters)):
    return filter

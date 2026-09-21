from fastapi import FastAPI, Request
from middle.mdlware import *#middleware_one,middleware_two


app = FastAPI()




# app.middleware("http")(middleware_one)
# app.middleware("http")(middleware_two)
#app.middleware("http")(path_middleware)
#app.add_middleware(MyMiddleware)
app.add_middleware(LoggingMiddleware)

@app.get("/")
async def home():
    print("Inside endpoint")
    return {"message": "Hello"}




#Simple Path-Specific Middleware
@app.get("/admin")
async def admin():
    return {"message": "Admin page"}


@app.get("/products")
async def products():
    return {"message": "Products"}


# @app.middleware("http")#"हा function HTTP middleware म्हणून वापर."
# async def my_middleware(request: Request, call_next):#Client ने पाठवलेली request.

#     print("Before endpoint")

#     response = await call_next(request)#Request ला पुढच्या processing कडे पाठव.जर call_next() call केला नाही तर request पुढे endpoint पर्यंत जाणार नाही.

#     print("After endpoint")

#     return response





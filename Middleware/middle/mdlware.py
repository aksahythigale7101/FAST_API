from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Scope, Receive, Send


class MyMiddleware(
    BaseHTTPMiddleware
):  # BaseHTTPMiddleware हा Starlette कडून मिळणारा base class आहे.

    async def dispatch(self, request, call_next):

        print("Before request")

        response = await call_next(request)

        print("After request")

        return response


async def middleware_one(request, call_next):

    print("M1 Before")

    response = await call_next(request)

    print("M1 After")

    return response


async def middleware_two(request, call_next):

    print("M2 Before")

    response = await call_next(request)

    print("M2 After")

    return response


# Simple Path-Specific Middleware
async def path_middleware(request, call_next):

    # if request.url.path == "/admin":
    #     print("Admin middleware executed")

    if request.url.path in ["/admin", "/users"]:
        print("Special middleware logic")

    response = await call_next(request)

    return response

#Async Server Gateway Interface
class LoggingMiddleware:

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):

        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        print("Before Request")
        print("Method:", scope["method"])
        print("Path:", scope["path"])

        await self.app(scope, receive, send)

        print("After Response")

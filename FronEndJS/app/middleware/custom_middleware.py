
import time
import uuid

from fastapi import Request


async def request_id_middleware(request: Request, call_next):

    # Generate unique request ID
    request_id = str(uuid.uuid4())

    # Store request ID
    request.state.request_id = request_id

    # Send request to next process
    response = await call_next(request)

    # Add request ID to response header
    response.headers["X-Request-ID"] = request_id

    return response


async def logging_middleware(request: Request, call_next):

    # Start timer
    start = time.perf_counter()

    # Send request to next process
    response = await call_next(request)

    # Calculate execution time
    process_time = time.perf_counter() - start

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time:.4f}s"
    )

    return response
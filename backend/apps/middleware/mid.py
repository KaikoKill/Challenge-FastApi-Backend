from fastapi import Request
import time

async def time_response(request: Request, call_next):
    time_start = time.perf_counter()
    response = await call_next(request)
    time_end = time.perf_counter() - time_start
    res = {
        "Request": request.method,
        "completed_in": time_end
    }
    print(res)
    return response
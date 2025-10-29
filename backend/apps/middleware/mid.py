from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware('http')
async def time_response(request: Request, call_next):
    time_start = time.perf_counter()
    response = await call_next(Request)
    time_end = time.perf_counter() - time_start
    res = {
        "Request": Request.method,
        "completed_in": time_end
    }
    print(res)
    return response
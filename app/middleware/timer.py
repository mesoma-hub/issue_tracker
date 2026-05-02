import time
from fastapi import Request

# perf_counter is a high-resolution timer that provides the most precise time measurement available on the system.
async def timing_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start_time:.4f} seconds"
    return response
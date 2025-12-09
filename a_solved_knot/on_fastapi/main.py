"""
Docstring for a_solved_knot.on_fastapi.main

How to run:

(.venv) PS C:\Temp\python\a_solved_knot\on_fastapi> uvicorn main:app --reload
"""
import logging
import time

from asgi_correlation_id import CorrelationIdMiddleware
from calculator.calculator import add
from configuration import DevConfig
from fastapi import FastAPI, Request
from logging_configuration import configure_logging

config = DevConfig()

configure_logging(config)


logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    response_time = time.perf_counter() - start_time
    logger.info(
        f"{request.method} {request.url.path} {response.status_code} {response_time:.3f}s"
    )
    return response



@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/add/")
async def read_item(a: int, b: int):
    result = add(a, b)
    """
    Usage: http://127.0.0.1:8000/add/?a=42&b=43
    """
    return {"a": a, "b": b, "result": result}

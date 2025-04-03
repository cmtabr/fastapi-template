from fastapi import FastAPI

from contextlib import asynccontextmanager

from utils import Logger

_logger = Logger(logger_name=__name__).logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI app.
    This is where you can set up and tear down resources.
    """
    _logger.info("Starting up FastAPI app")
    yield
    _logger.info("Shutting down FastAPI app")

app = FastAPI(
    title="FastAPI Template",
    summary="A template for FastAPI projects",
    version="1.0.0",
    contact={
        "name": "cmtabr",
        "url": "https://github.com/cmtabr",
        "email": "cmtabr@gmail.com",
    },
    lifespan=lifespan
)

@app.get("/", status_code=200, tags=["Health Check"])
async def health_check() -> dict:
    _logger.info(
        "Health check endpoint called"
    )
    return {"Message": "Application running"}

import uvicorn

from fastapi import FastAPI
from core.config import settings
from contextlib import asynccontextmanager
from api import router as api_router

from core.db.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await db_helper.dispose()


app = FastAPI(
    title="ApiSpyTime",
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello"}


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )

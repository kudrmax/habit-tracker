from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from core.config import settings
from models import db_helper


# from api_v1 import router as router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
# main_app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run('main:main_app', reload=True)

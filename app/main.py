from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from core.config import settings
from models import Base
from models import db_helper
from api import router as api_router


# from api_v1 import router as router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(api_router)
# main_app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )

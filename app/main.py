import uvicorn

from fastapi import FastAPI

from core.config import settings
from models import Base #, db_helper
# from api_v1 import router as router_v1

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # async with db_helper.engine.begin() as conn:
#     #     await conn.run_sync(Base.metadata.create_all)
#     yield


# app = FastAPI(lifespan=lifespan)
app = FastAPI()
# app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)

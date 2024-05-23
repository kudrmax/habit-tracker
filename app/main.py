from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from core.config import settings
from models import Base
from models import db_helper
from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # async with db_helper.engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
    docs_url='/docs' if not settings.run.static_docs else None,
    redoc_url='/redoc' if not settings.run.static_docs else None,
)
main_app.include_router(api_router)


if settings.run.static_docs:
    from fastapi.openapi.docs import (
        get_redoc_html,
        get_swagger_ui_html,
        get_swagger_ui_oauth2_redirect_html,
    )
    from fastapi.staticfiles import StaticFiles

    main_app.mount("/static", StaticFiles(directory="static"), name="static")


    @main_app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=main_app.openapi_url,
            title=main_app.title + " - Swagger UI",
            oauth2_redirect_url=main_app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )


    @main_app.get(main_app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()


    @main_app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=main_app.openapi_url,
            title=main_app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
        )

if __name__ == "__main__":
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )

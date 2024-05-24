from fastapi import APIRouter

from config import settings

from .user.views import router as user_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(user_router)

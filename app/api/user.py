from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.user import get_all_users
from models import db_helper
from schemas.user import UserRead

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/", response_model=list[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_all_users(session=session)

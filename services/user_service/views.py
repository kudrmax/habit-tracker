from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import get_all_users
from .crud import create_user
from models import db_helper
from .schemas import UserRead, UserCreate

router = APIRouter(tags=["user"], prefix="/user")


@router.get("/", response_model=list[UserRead])
async def get_users(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        # session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_all_users(session=session)


@router.post("/", response_model=UserRead)
async def create_user_api(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        new_user: UserCreate,
):
    user = await create_user(session=session, new_user=new_user)
    return user

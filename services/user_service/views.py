from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import get_all_users
from .crud import create_user, get_user_by_id, delete_user
from models import db_helper
from .schemas import UserRead, UserCreate

router = APIRouter(tags=["user"], prefix="/user")


@router.get("/", response_model=list[UserRead])
async def get_all_users_endpoint(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        # session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_all_users(session=session)


@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id_endpoint(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_id: int,
):
    db_user = await get_user_by_id(session=session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return db_user


@router.post("/", response_model=UserRead)
async def create_user_endpoint(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        new_user: UserCreate,
):
    user = await create_user(session=session, new_user=new_user)
    return user


@router.delete("/{user_id}")
async def delete_user_endpoint(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_id: int,
):
    deleted_user = await delete_user(session=session, user_id=user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return deleted_user
    # return UserRead(id=10, username='123')

# @router.post("/", response_model=UserRead)
# async def update_user_endpoint(
#         session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
#         new_user: UserCreate,
# ):
#     user = await create_user(session=session, new_user=new_user)
#     return user

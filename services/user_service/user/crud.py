from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .schemas import UserCreate, UserUpdate


async def get_all_users(session: AsyncSession) -> List[User]:
    query = select(User).order_by(User.id)
    result = await session.execute(query)
    users: List[User] = list(result.scalars())
    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> Optional[User]:
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    user: User = result.scalar_one_or_none()
    return user


async def create_user(session: AsyncSession, new_user: UserCreate) -> User:
    user_dict = new_user.dict()
    if 'username' in user_dict:
        user_dict['username'] = user_dict['username'].lower()
    user = User(**user_dict)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(session: AsyncSession, user_id: int) -> Optional[User]:
    user: User = await get_user_by_id(session, user_id)
    if user:
        await session.delete(user)
        await session.commit()
        return user
    return None


async def update_user(
        session: AsyncSession,
        user_id: int,
        new_user: UserUpdate) -> User:
    user: User = await get_user_by_id(session, user_id)
    if not user:
        return None
    new_user_dict = new_user.model_dump(exclude_unset=True)
    for key, value in new_user_dict.items():
        setattr(user, key, value)
    await session.commit()
    await session.refresh(user)
    return user

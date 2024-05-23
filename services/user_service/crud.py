from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user_schema import UserCreate


async def get_all_users(session: AsyncSession) -> List[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return list(result.all())


async def create_user(session: AsyncSession, new_user: UserCreate) -> User:
    user = User(**new_user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

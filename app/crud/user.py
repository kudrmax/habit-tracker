from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User


async def get_all_users(session: AsyncSession) -> List[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return list(result.all())

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base


class User(Base):
    username: Mapped[int] = mapped_column(String(40), unique=True)

    profile: Mapped['Profile'] = relationship(back_populates='user')


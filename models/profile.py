from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from .base import Base


class Profile(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))

    user: Mapped['User'] = relationship(back_populates='profile')

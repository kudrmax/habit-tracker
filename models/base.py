from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from config import settings

class Base(DeclarativeBase):
    """
    Класс, который будет являться родителем для любой таблицы в базе данных

    Атрибуты:
    __tablename__: автоматически генерируемое имя таблице на основе названия класса
    id: уникальный идентификатор
    """
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)

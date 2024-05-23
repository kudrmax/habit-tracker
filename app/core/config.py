from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

BASE_DIR = Path(__file__).resolve().parent.parent


class RunSettings(BaseModel):
    static_docs: bool = True
    host: str = 'localhost'
    port: int = 7878


class ApiPrefixSettings(BaseModel):
    prefix: str = '/api'


class DbSettings(BaseModel):
    # model_config = SettingsConfigDict(
    #     env_file='.env',
    #     case_sensitive=False,
    #     env_nested_delimiter="__",
    #     env_prefix="FASTAPI__"
    # )
    # url: PostgresDsn
    url: str = 'postgresql+asyncpg://user:password@localhost:7777/shop'
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {  # правила, для создания имен для более сложных штук в SQLAlchemy/alembic
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: ApiPrefixSettings = ApiPrefixSettings()
    db: DbSettings = DbSettings()


settings = Settings()

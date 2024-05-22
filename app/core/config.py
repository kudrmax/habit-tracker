from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic import BaseModel, PostgresDsn

BASE_DIR = Path(__file__).resolve().parent.parent


class RunSettings(BaseModel):
    host: str = 'localhost'
    port: int = 5432


class ApiPrefixSettings(BaseModel):
    prefix: str = 'api'


class DbSettings(BaseModel):
    url: PostgresDsn
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: ApiPrefixSettings = ApiPrefixSettings()
    db: DbSettings


settings = Settings()

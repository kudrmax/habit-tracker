from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'db.sqlite3'


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db: DbSettings = DbSettings()


settings = Settings()

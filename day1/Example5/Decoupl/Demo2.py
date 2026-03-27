from dataclasses import dataclass
from typing import Literal
from decouple import config

@dataclass
class Settings:
    env: Literal["dev", "prod"]
    debug: bool
    db_url: str

settings = Settings(
    env=config("ENV", default="dev"),
    debug=config("DEBUG", cast=bool, default=False),
    db_url=config("DATABASE_URL")
)
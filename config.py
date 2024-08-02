from typing import Any, Dict, Optional
from dotenv import load_dotenv
from pydantic import field_validator, PostgresDsn
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DEBUG: bool = True

    DATABASE_SQLITE: bool
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_URL: Optional[str] = None

    @field_validator('DATABASE_URL', mode="before")
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        """Create URL for DB connect"""
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme='postgres',
            username=values.data.get('DATABASE_USER'),
            password=values.data.get('DATABASE_PASSWORD'),
            host=values.data.get('DATABASE_HOST'),
            # port=values.data.get('DATABASE_PORT'),
            path=f'{values.data.get("DATABASE_NAME") or ""}',
        ).unicode_string()


settings = Settings()

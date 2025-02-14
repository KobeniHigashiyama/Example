from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", " PROD"]
    LOG_LEVEL : str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str

    ALGORITHM: str
    REDIS_HOST: str
    REDIS_PORT: int

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = ".env"  # Указываем файл для загрузки переменных окружения


settings = Settings()

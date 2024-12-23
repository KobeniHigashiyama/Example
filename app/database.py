from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


engine = create_async_engine(settings.DATABASE_URL)

# Создаём фабрику сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс для моделей
class Base(DeclarativeBase):
    pass



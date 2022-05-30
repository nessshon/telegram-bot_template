from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from bot.config import config
from bot.database.data import BASE_DIR


def get_engine(postgresql: bool = False) -> AsyncEngine:
    return create_async_engine(
        f'postgresql+asyncpg://{config.db.DB_USER}:{config.db.DB_PASS}@{config.db.DB_HOST}/{config.db.DB_NAME}'
    ) if postgresql else create_async_engine(
        f'sqlite+aiosqlite:///{BASE_DIR}/file/database.sqlite'
    )


engine = get_engine(postgresql=True)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

from .data.buttons import data_buttons
from .data.messages import data_messages
from .loader import engine, async_session_maker
from .models import Base


async def database_manage(sync_tables: bool = False,
                          write_buttons: bool = False,
                          write_messages: bool = False,
                          ):
    async def run_sync_tables():
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    async def run_write_buttons():
        async with async_session_maker() as session:
            session.add_all(data_buttons)
            await session.commit()

    async def run_write_messages():
        async with async_session_maker() as session:
            session.add_all(data_messages)
            await session.commit()

    if sync_tables:
        await run_sync_tables()

    if write_buttons:
        await run_write_buttons()

    if write_messages:
        await run_write_messages()

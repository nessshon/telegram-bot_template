from sqlalchemy import Column, Integer, String, select, update, DateTime, func, delete

from bot.database.loader import async_session_maker
from bot.database.models import Base


class SponsorshipModel(Base):
    __tablename__ = "_sponsorship"

    id = Column(Integer, primary_key=True)

    status = Column(
        String,
        nullable=False)
    chat_id = Column(
        String,
        nullable=False)
    chat_title = Column(
        String,
        nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=func.now())

    @classmethod
    async def add(cls,
                  status: str,
                  chat_id: str,
                  chat_title: str
                  ):
        async with async_session_maker() as session:
            session.add(cls(status=status,
                            chat_id=chat_id,
                            chat_title=chat_title))
            await session.commit()

    @classmethod
    async def delete(cls, chat_id: str):
        async with async_session_maker() as session:
            await session.execute(delete(cls).where(cls.chat_id == chat_id))
            await session.commit()

    @classmethod
    async def get(cls, chat_id: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls).where(cls.chat_id == chat_id))
            return query.scalar()

    @classmethod
    async def get_chat_id_chat_title_all(cls):
        async with async_session_maker() as session:
            chat_id_all = await session.execute(
                select(cls.chat_id).order_by(cls.id.asc()))
            chat_title_all = await session.execute(
                select(cls.chat_title).order_by(cls.id.asc()))
            return dict(zip([i[0] for i in chat_id_all.all()], [i[0] for i in chat_title_all.all()]))

    @classmethod
    async def get_active_chat_all(cls):
        async with async_session_maker() as session:
            chat_id_all = await session.execute(
                select(cls.chat_id).where(cls.status == 'active').order_by(cls.id.asc()))
            chat_title_all = await session.execute(
                select(cls.chat_title).where(cls.status == 'active').order_by(cls.id.asc()))
            return dict(zip([i[0] for i in chat_id_all.all()], [i[0] for i in chat_title_all.all()]))

    @classmethod
    async def update_chat_id(cls, chat_id: str, new_chat_id: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.chat_id == chat_id).values(chat_id=new_chat_id))
            await session.commit()

    @classmethod
    async def get_status(cls, chat_id: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.status).where(cls.chat_id == chat_id))
            return query.scalar()

    @classmethod
    async def update_status(cls, chat_id: str, status: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.chat_id == chat_id).values(status=status))
            await session.commit()

    @classmethod
    async def get_chat_title(cls, chat_id: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.chat_title).where(cls.chat_id == chat_id))
            return query.scalar()

    @classmethod
    async def update_chat_title(cls, chat_id: str, chat_title: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.chat_id == chat_id).values(chat_title=chat_title))
            await session.commit()

    @classmethod
    async def get_count(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls))
            return query.scalar()

    @classmethod
    async def get_count_active(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.status == 'active'))
            return query.scalar()

    @classmethod
    async def get_count_inactive(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.status == 'inactive'))
            return query.scalar()

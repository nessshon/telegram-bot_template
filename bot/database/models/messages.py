from sqlalchemy import Column, String, Integer, select, update, func

from bot.database.loader import async_session_maker
from bot.database.models import Base


class MessageModel(Base):
    __tablename__ = "_messages"
    id = Column(Integer, primary_key=True)

    code = Column(
        String,
        nullable=False)
    desc = Column(
        String,
        nullable=False)
    ru = Column(
        String,
        nullable=False)

    @classmethod
    async def add(cls,
                  code: str,
                  desc: str,
                  ru: str,
                  ):
        async with async_session_maker() as session:
            session.add(cls(code=code,
                            desc=desc,
                            ru=ru))
            await session.commit()

    @classmethod
    async def get(cls, code: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls).where(cls.code == code))
            return query.scalar()

    @classmethod
    async def get_text(cls, code: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.ru).where(cls.code == code))

            return query.scalar()

    @classmethod
    async def update(cls, code: str, text: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.code == code).values(ru=text))

            await session.commit()

    @classmethod
    async def get_code_desc_all(cls):
        async with async_session_maker() as session:
            code_all = await session.execute(select(cls.code).order_by(cls.id.desc()))
            desc_all = await session.execute(select(cls.desc).order_by(cls.id.desc()))
            return dict(zip([i[0] for i in code_all.all()], [i[0] for i in desc_all.all()]))

    @classmethod
    async def get_code_desc_filer_all(cls, text: str):
        async with async_session_maker() as session:
            code_all = await session.execute(
                select(cls.code).filter(cls.ru.ilike(f"%{text}%")).limit(5).order_by(cls.id.desc()))
            desc_all = await session.execute(
                select(cls.desc).filter(cls.ru.ilike(f"%{text}%")).limit(5).order_by(cls.id.desc()))
            return dict(zip([i[0] for i in code_all.all()], [i[0] for i in desc_all.all()]))

    @classmethod
    async def get_code_all(cls):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.code).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_desc(cls, code: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.desc).where(cls.code == code))
            return query.scalar()

    @classmethod
    async def get_desc_all(cls):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.desc).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_count(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls))
            return query.scalar()

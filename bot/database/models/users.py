from sqlalchemy import Column, BigInteger, Integer, String, DateTime, func, update, select, cast

from bot.database.loader import async_session_maker
from bot.database.models import Base


class UserModel(Base):
    __tablename__ = "_users"

    id = Column(Integer, primary_key=True)

    state = Column(
        String,
        nullable=False)
    user_id = Column(
        BigInteger,
        nullable=False)
    first_name = Column(
        String,
        nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=func.now())

    @classmethod
    async def add(cls,
                  state: str,
                  user_id: int,
                  first_name: str,
                  ):
        async with async_session_maker() as session:
            session.add(cls(state=state,
                            user_id=user_id,
                            first_name=first_name))
            await session.commit()

    @classmethod
    async def get(cls, user_id: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def join(cls, user_id: int, state: str = 'joined'):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(state=state))
            await session.commit()

    @classmethod
    async def kick(cls, user_id: int, state: str = 'kicked'):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(state=state))
            await session.commit()

    @classmethod
    async def block(cls, user_id: int, state: str = 'blocked'):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(state=state))
            await session.commit()

    @classmethod
    async def get_user_id_all(cls):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.user_id).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_user_id_first_name_all(cls):
        async with async_session_maker() as session:
            user_id = await session.execute(select(cls.user_id).order_by(cls.id.desc()))
            first_name = await session.execute(select(cls.first_name).order_by(cls.id.desc()))
            return dict(zip([i[0] for i in user_id.all()], [i[0] for i in first_name.all()]))

    @classmethod
    async def get_user_id_first_name_filter_all(cls, text: str):
        async with async_session_maker() as session:
            if text.isdigit():
                user_id = await session.execute(
                    select(cls.user_id).filter(cast(cls.user_id, String).ilike(f'%{text}%')).order_by(cls.id.desc()))
                first_name = await session.execute(
                    select(cls.first_name).filter(cast(cls.user_id, String).ilike(f'%{text}%')).order_by(cls.id.desc()))
                return dict(zip([i[0] for i in user_id.all()], [i[0] for i in first_name.all()]))
            else:
                user_id = await session.execute(
                    select(cls.user_id).filter(cls.first_name.ilike(f"%{text}%")).order_by(cls.id.desc()))
                first_name = await session.execute(
                    select(cls.first_name).filter(cls.first_name.ilike(f"%{text}%")).order_by(cls.id.desc()))
                return dict(zip([i[0] for i in user_id.all()], [i[0] for i in first_name.all()]))

    @classmethod
    async def get_state(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.state).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def get_first_name(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.first_name).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def update_first_name(cls, user_id: int, first_name: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(first_name=first_name))
            await session.commit()

    @classmethod
    async def get_first_name_all(cls):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.first_name).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_created_at(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.created_at).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def get_count(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls))
            return query.scalar()

    @classmethod
    async def get_count_joined(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.state == 'joined'))
            return query.scalar()

    @classmethod
    async def get_count_kicked(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.state == 'kicked'))
            return query.scalar()

    @classmethod
    async def get_count_blocked(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.state == 'blocked'))
            return query.scalar()

    @classmethod
    async def is_blocked(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.state).where(cls.user_id == user_id))
            return query.scalar() == 'blocked'

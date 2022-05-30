from sqlalchemy import Column, Integer, BigInteger, String, func, select, delete, update, DateTime

from bot.database.loader import async_session_maker
from bot.database.models import Base


class AdminModel(Base):
    __tablename__ = "_admins"
    id = Column(Integer, primary_key=True)

    role = Column(
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
                  role: str,
                  user_id: int,
                  first_name: str
                  ):
        async with async_session_maker() as session:
            session.add(cls(role=role,
                            user_id=user_id,
                            first_name=first_name))
            await session.commit()

    @classmethod
    async def get(cls, user_id: str):
        async with async_session_maker() as session:
            query = await session.execute(select(cls).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def delete(cls, user_id: int):
        async with async_session_maker() as session:
            await session.execute(delete(cls).where(cls.user_id == user_id))
            await session.commit()

    @classmethod
    async def get_role(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.role).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def get_first_name(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.first_name).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def get_created_at(cls, user_id: int):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.created_at).where(cls.user_id == user_id))
            return query.scalar()

    @classmethod
    async def get_user_id_all(cls):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.user_id).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_role_moder_all(cls, role: str = 'moder'):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.user_id).where(cls.role == role).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def get_role_admin_all(cls, role: str = 'admin'):
        async with async_session_maker() as session:
            query = await session.execute(select(cls.user_id).where(cls.role == role).order_by(cls.id.desc()))
            return [i[0] for i in query.all()]

    @classmethod
    async def update_id(cls, user_id: int, new_user_id: int):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(user_id=new_user_id))
            await session.commit()

    @classmethod
    async def update_first_name(cls, user_id: int, first_name: str):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(first_name=first_name))
            await session.commit()

    @classmethod
    async def update_role_moder(cls, user_id: int, role: str = 'moder'):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(role=role))
            await session.commit()

    @classmethod
    async def update_role_admin(cls, user_id: int, role: str = 'admin'):
        async with async_session_maker() as session:
            await session.execute(update(cls).where(cls.user_id == user_id).values(role=role))
            await session.commit()

    @classmethod
    async def get_count(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls))
            return query.scalar()

    @classmethod
    async def get_count_admin(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.role == 'admins'))
            return query.scalar()

    @classmethod
    async def get_count_moder(cls):
        async with async_session_maker() as session:
            query = await session.execute(select([func.count()]).select_from(cls).where(cls.role == 'moder'))
            return query.scalar()

    @classmethod
    async def get_user_id_first_name_all(cls):
        async with async_session_maker() as session:
            user_id_list = await session.execute(select(cls.user_id).order_by(cls.role))
            first_name_list = await session.execute(select(cls.first_name).order_by(cls.role))
            return dict(zip([i[0] for i in user_id_list.all()], [i[0] for i in first_name_list.all()]))

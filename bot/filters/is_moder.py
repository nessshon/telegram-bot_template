from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.database import db


class IsModer(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in await db.admin.get_role_moder_all()

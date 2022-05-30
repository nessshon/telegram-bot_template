from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.config import config


class IsCreator(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        return str(message.from_user.id) == config.bot.CREATOR_ID

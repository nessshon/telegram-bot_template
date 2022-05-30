from contextlib import suppress

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.database import db

from aiogram.types import (Message,
                           CallbackQuery, User)

from aiogram.utils.exceptions import (BotBlocked,
                                      ChatNotFound)


class BlockingMiddleware(BaseMiddleware):

    def __init__(self):
        super(BlockingMiddleware, self).__init__()

    async def on_pre_process_message(self, message: Message, data: dict):
        user = User.get_current()

        if await db.user.is_blocked(user_id=user.id):
            with suppress(ChatNotFound, BotBlocked):
                text = await db.message.get_text(code='blocked')

                await message.answer(text=text)
            raise CancelHandler()

    async def on_pre_process_callback_query(self, call: CallbackQuery, data: dict):
        user = User.get_current()

        if await db.user.is_blocked(user_id=user.id):
            with suppress(ChatNotFound, BotBlocked):
                text = await db.message.get_text(code='blocked')

                await call.answer(text=text)
            raise CancelHandler()

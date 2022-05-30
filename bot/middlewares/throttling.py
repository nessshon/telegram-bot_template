from aiogram import Dispatcher
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.database import db

from aiogram.types import (Message,
                           CallbackQuery)

from aiogram.dispatcher.handler import (CancelHandler,
                                        current_handler)


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, message_limit=0.5, call_limit=0.5, key='default'):
        self.message_limit = message_limit
        self.call_limit = call_limit
        self.default_key = key
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:
            throttling_key = getattr(handler, "throttling_key", None)
            key = throttling_key if throttling_key else self.default_key
            limit = getattr(handler, "throttling_rate_limit", self.message_limit)

        else:
            limit = self.message_limit
            key = self.default_key

        try:
            await dispatcher.throttle(key, rate=limit)

        except Throttled:
            await message.delete()

            raise CancelHandler()

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:
            throttling_key = getattr(handler, "throttling_key", None)
            key = throttling_key if throttling_key else self.default_key
            limit = getattr(handler, "throttling_rate_limit", self.call_limit)

        else:
            limit = self.call_limit
            key = self.default_key

        try:
            await dispatcher.throttle(key, rate=limit)

        except Throttled:
            text = await db.message.get_text(code='throttling')

            await call.answer(text=text.format(limit=limit))
            raise CancelHandler()

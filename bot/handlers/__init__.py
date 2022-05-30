from aiogram import Dispatcher

from bot.handlers.callback import callback_handler
from bot.keyboards.callback_data import cdata


def register_inline_handlers(dp: Dispatcher):
    pass


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        callback_handler,
        text=[cdata.hide],
        state='*')

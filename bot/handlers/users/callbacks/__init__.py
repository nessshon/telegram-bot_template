from aiogram import Dispatcher

from bot.handlers.users.callbacks.sponsored import sponsored_callback_handler

from bot.states import states


def register_user_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        sponsored_callback_handler,
        state=states.user.sponsored)

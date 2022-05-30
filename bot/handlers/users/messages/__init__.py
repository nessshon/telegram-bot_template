from aiogram import Dispatcher

from bot.filters import IsPrivate
from bot.handlers.users.messages.main import main_message_handler
from bot.handlers.users.messages.sponsored import sponsored_message_handler

from bot.states import states


def register_user_message_handlers(dp: Dispatcher):
    dp.register_message_handler(
        main_message_handler, IsPrivate(),
        state=states.user.main,
        content_types='any')
    dp.register_message_handler(
        sponsored_message_handler, IsPrivate(),
        state=states.user.sponsored,
        content_types='any')

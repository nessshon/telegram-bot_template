from aiogram import Dispatcher

from bot.filters import IsPrivate
from bot.handlers.users.commands.start import start_command


def register_user_command_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_command, IsPrivate(),
        commands='start',
        state='*')

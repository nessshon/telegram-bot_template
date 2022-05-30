from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.handlers.admins.functions.users import users
from bot.utils.bot.message import delete_message


async def users_command(message: Message, state: FSMContext):
    await users(message=message, state=state)

    await delete_message(message=message)

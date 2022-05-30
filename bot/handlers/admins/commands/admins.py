from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.handlers.admins.functions.admins import admins
from bot.utils.bot.message import delete_message


async def admins_command(message: Message, state: FSMContext):
    await admins(message=message, state=state)

    await delete_message(message=message)

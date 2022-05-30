from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.utils.bot.message import delete_message
from bot.handlers.admins.functions.sponsorship import sponsorship


async def sponsorship_command(message: Message, state: FSMContext):
    await sponsorship(message=message, state=state)

    await delete_message(message=message)

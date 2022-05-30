from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.handlers.admins.functions.newsletter import newsletter
from bot.utils.bot.message import delete_message


async def newsletter_command(message: Message, state: FSMContext):
    await newsletter(message=message, state=state)

    await delete_message(message=message)

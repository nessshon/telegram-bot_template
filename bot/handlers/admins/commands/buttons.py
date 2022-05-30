from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.handlers.admins.functions.buttons import buttons
from bot.utils.bot.message import delete_message


async def buttons_command(message: Message, state: FSMContext):
    await buttons(message=message, state=state)

    await delete_message(message=message)

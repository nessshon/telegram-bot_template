from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.handlers.admins.functions.messages import messages
from bot.utils.bot.message import delete_message


async def messages_command(message: Message, state: FSMContext):
    await messages(message=message, state=state)

    await delete_message(message=message)

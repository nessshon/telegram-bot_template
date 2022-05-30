from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot.utils.bot.message import delete_message


async def main_message_handler(message: Message, state: FSMContext):
    await delete_message(message=message)

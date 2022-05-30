from aiogram.types import Message

from bot.utils.bot.message import delete_message


async def sponsored_message_handler(message: Message):
    await delete_message(message)


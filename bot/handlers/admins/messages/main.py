from aiogram.types import Message

from bot.utils.bot.message import delete_message


async def main_admin_message_handler(message: Message):
    await delete_message(message=message)

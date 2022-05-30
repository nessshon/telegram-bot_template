from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.handlers.admins.functions.main import main_admin
from bot.utils.bot.message import delete_message


async def admin_command(message: Message, state: FSMContext):
    await main_admin(message=message, state=state)

    await delete_message(message=message)

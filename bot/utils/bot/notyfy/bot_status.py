from contextlib import suppress

from aiogram.utils.exceptions import (ChatNotFound,
                                      BotBlocked)

from bot.config import config
from bot.keyboards import keyboards
from bot.loader import bot
from bot.texts import texts


async def startup():
    with suppress(ChatNotFound, BotBlocked):
        await bot.send_message(
            chat_id=config.bot.CREATOR_ID,
            text=texts.message.bot_started,
            reply_markup=await keyboards.inline.delete())


async def shutdown():
    with suppress(ChatNotFound, BotBlocked):
        await bot.send_message(
            chat_id=config.bot.CREATOR_ID,
            text=texts.message.bot_stopped,
            reply_markup=await keyboards.inline.delete())

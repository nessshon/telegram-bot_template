import json
import logging
import traceback

from contextlib import suppress
from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import User
from aiogram.utils.exceptions import (MessageIsTooLong,
                                      ChatNotFound,
                                      BotBlocked)

from aiogram.utils.markdown import hcode, hlink, hbold

from bot.config import config
from bot.keyboards import keyboards
from bot.loader import bot
from bot.texts import texts


async def error_handler(update, exception):
    logging.exception(f'Update: {update} \n{exception}')
    user = User.get_current()

    with suppress(ChatNotFound, BotBlocked):
        await bot.send_message(
            chat_id=config.bot.CREATOR_ID,
            text=texts.message.error_info.format(
                user=hlink(title=user.first_name, url=user.url),
                datetime=hbold(datetime.now().strftime('%Y-%m-%d %H:%m')),
                update=hcode(
                    json.dumps(dict(update),
                               indent=1,
                               sort_keys=True,
                               ensure_ascii=False)),
                exception=hcode(exception)),
            reply_markup=await keyboards.inline.delete())

    with suppress(MessageIsTooLong, ChatNotFound, BotBlocked):
        await bot.send_message(
            chat_id=config.bot.CREATOR_ID,
            text=texts.message.error_traceback.format(
                traceback=hcode(traceback.format_exc())),
            reply_markup=await keyboards.inline.delete())

    return


def register_errors_handler(dp: Dispatcher):
    dp.register_errors_handler(error_handler)

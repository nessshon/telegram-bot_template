from contextlib import suppress

from aiogram.types import (User,
                           Message)

from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import ChatNotFound, BotBlocked
from aiogram.utils.markdown import hlink

from bot.config import config
from bot.database import db
from bot.handlers.users.functions.sponsored import get_sponsored, sponsored
from bot.loader import bot

from bot.texts import texts

from bot.utils.bot.message import delete_message
from bot.handlers.users.functions.main import main


async def start_command(message: Message, state: FSMContext):
    user = User.get_current()

    if user.id in await db.user.get_user_id_all():
        await main(message, state=state)

    else:
        status = 'joined'

        await db.user.add(
            state=status,
            user_id=user.id,
            first_name=user.first_name)

        with suppress(ChatNotFound, BotBlocked):
            await bot.send_message(
                chat_id=config.bot.CREATOR_ID,
                text=texts.message.user_started_bot.format(
                    user=hlink(
                        title=message.from_user.first_name,
                        url=message.from_user.url)))

        sponsored_data = await get_sponsored()

        if any(sponsored_data):
            await sponsored(
                message=message,
                state=state,
                sponsored_data=sponsored_data)

        else:
            await main(message=message, state=state)

    await delete_message(message=message)

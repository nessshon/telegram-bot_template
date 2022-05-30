from contextlib import suppress

from aiogram import Dispatcher
from aiogram.types import ChatMemberUpdated, ChatMemberStatus
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from aiogram.utils.markdown import hlink

from bot.config import config
from bot.database import db
from bot.loader import bot
from bot.texts import texts


async def send_notify(update: ChatMemberUpdated, text: str):
    with suppress(ChatNotFound, BotBlocked):
        await bot.send_message(
            chat_id=config.bot.CREATOR_ID,
            text=text.format(
                user=hlink(
                    title=update.from_user.first_name,
                    url=update.from_user.url)))


async def update_users_status_handler(update: ChatMemberUpdated):
    if update.new_chat_member.status == ChatMemberStatus.KICKED:
        await send_notify(
            update=update,
            text=texts.message.user_stopped_bot)
        await db.user.kick(user_id=update.from_user.id)
    if update.new_chat_member.status == ChatMemberStatus.MEMBER:
        await send_notify(
            update=update,
            text=texts.message.user_restarted_bot)
        await db.user.join(user_id=update.from_user.id)


def register_user_status_handlers(dp: Dispatcher):
    dp.register_my_chat_member_handler(
        update_users_status_handler, state='*'
    )

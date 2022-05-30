from contextlib import suppress

from aiogram.types import (BotCommand,
                           BotCommandScopeChat,
                           BotCommandScopeAllGroupChats,
                           BotCommandScopeAllPrivateChats)

from aiogram.utils.exceptions import (BotBlocked,
                                      ChatNotFound)

from bot.config import config
from bot.database import db
from bot.loader import bot

creator_commands = [
    BotCommand('admin', 'Панель администратора'),
    BotCommand('admins', 'Администраторы'),
    BotCommand('users', 'Пользователи'),
    BotCommand('buttons', 'Кнопоки'),
    BotCommand('messages', 'Сообщения'),
    BotCommand('newsletter', 'Рассылка'),
    BotCommand('sponsorship', 'Спонсорка'),
]

admin_commands = [
    BotCommand('admin', 'Панель администратора'),
]

user_commands = [
    BotCommand('start', 'Перезапустить бота'),
]

group_commands = [
    BotCommand('id', 'Узнать ID группы')
]


async def setup():
    await bot.set_my_commands(
        commands=user_commands,
        scope=BotCommandScopeAllPrivateChats())

    await bot.set_my_commands(
        commands=group_commands,
        scope=BotCommandScopeAllGroupChats())

    with suppress(ChatNotFound, BotBlocked):
        await bot.set_my_commands(
            commands=user_commands + creator_commands,
            scope=BotCommandScopeChat(chat_id=config.bot.CREATOR_ID))

    for user_id in await db.admin.get_role_admin_all():
        with suppress(ChatNotFound, BotBlocked):
            await bot.set_my_commands(
                commands=user_commands + admin_commands,
                scope=BotCommandScopeChat(chat_id=user_id))

    for user_id in await db.admin.get_role_moder_all():
        with suppress(ChatNotFound, BotBlocked):
            await bot.set_my_commands(
                commands=user_commands + admin_commands,
                scope=BotCommandScopeChat(chat_id=user_id))

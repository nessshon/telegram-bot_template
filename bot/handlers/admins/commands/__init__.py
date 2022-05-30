from aiogram import Dispatcher

from bot.filters import IsAdmin, IsCreator, IsModer
from bot.handlers.admins.commands.admin import admin_command
from bot.handlers.admins.commands.admins import admins_command
from bot.handlers.admins.commands.messages import messages_command
from bot.handlers.admins.commands.buttons import buttons_command
from bot.handlers.admins.commands.newsletter import newsletter_command
from bot.handlers.admins.commands.sponsorship import sponsorship_command
from bot.handlers.admins.commands.users import users_command


def register_admin_command_handlers(dp: Dispatcher):
    dp.register_message_handler(
        admin_command, IsCreator() | IsAdmin() | IsModer(),
        commands='admin',
        state='*')
    # -----sponsorship
    dp.register_message_handler(
        sponsorship_command, IsCreator() | IsAdmin(),
        commands='sponsorship',
        state='*')
    # -----messages
    dp.register_message_handler(
        messages_command, IsCreator() | IsAdmin() | IsModer(),
        commands='messages',
        state='*')
    # -----buttons
    dp.register_message_handler(
        buttons_command, IsCreator() | IsAdmin() | IsModer(),
        commands='buttons',
        state='*')
    # -----newsletter
    dp.register_message_handler(
        newsletter_command, IsCreator() | IsAdmin() | IsModer(),
        commands='newsletter',
        state='*')
    # -----newsletter
    dp.register_message_handler(
        admins_command, IsCreator(),
        commands='admins',
        state='*')
    # -----users
    dp.register_message_handler(
        users_command, IsCreator() | IsAdmin(),
        commands='users',
        state='*')

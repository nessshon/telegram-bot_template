import locale
import logging

from bot.loader import dp
from bot.config import config

from bot.utils.bot import commands
from bot.utils.bot.notyfy import bot_status

from bot.scheduler.loader import scheduler
from bot.database.manage import database_manage


async def startup(dispatcher):
    locale.setlocale(
        locale.LC_TIME, "ru_RU.UTF8")
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    scheduler.start()
    await database_manage(
        sync_tables=True,
        write_buttons=True,
        write_messages=True)

    from bot.filters import setup_filters
    setup_filters(dispatcher)
    from bot.middlewares import setup_middlewares
    setup_middlewares(dispatcher)

    from bot.utils.bot.notyfy.error_status import register_errors_handler
    register_errors_handler(dispatcher)
    from bot.utils.bot.notyfy.member_status import register_user_status_handlers
    register_user_status_handlers(dispatcher)

    from bot.handlers import register_callback_handlers
    register_callback_handlers(dp)
    from bot.handlers import register_inline_handlers
    register_inline_handlers(dp)

    from bot.handlers.users.commands import register_user_command_handlers
    register_user_command_handlers(dp)

    from bot.handlers.admins.commands import register_admin_command_handlers
    register_admin_command_handlers(dp)

    from bot.handlers.users.callbacks import register_user_callback_handlers
    register_user_callback_handlers(dp)

    from bot.handlers.admins.callbacks import register_admin_callback_handlers
    register_admin_callback_handlers(dp)

    from bot.handlers.users.messages import register_user_message_handlers
    register_user_message_handlers(dp)

    from bot.handlers.admins.messages import register_admin_message_handlers
    register_admin_message_handlers(dp)

    await commands.setup()
    await bot_status.startup()
    await dp.reset_webhook()
    await dp.bot.set_webhook(
        url=f'{config.webhook.SITE}'
            f'{config.webhook.PATH}')


async def shutdown(dispatcher):
    session = await dispatcher.bot.get_session()

    await bot_status.shutdown()
    await dispatcher.storage.wait_closed()
    await dispatcher.storage.close()
    await session.close()

    scheduler.shutdown()

import logging

from aiogram.utils.executor import (start_webhook,
                                    start_polling)

from bot import on_
from bot.config import config
from bot.loader import dp


def start_bot(webhook: bool = False):
    if webhook:
        start_webhook(
            dispatcher=dp,
            webhook_path=config.webhook.PATH,
            skip_updates=True,
            on_startup=on_.startup,
            on_shutdown=on_.shutdown,
            host=config.webhook.HOST,
            port=config.webhook.PORT)
    else:
        start_polling(
            dispatcher=dp,
            skip_updates=True,
            reset_webhook=True,
            on_startup=on_.startup,
            on_shutdown=on_.shutdown)


try:
    start_bot(webhook=False)
except (KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")

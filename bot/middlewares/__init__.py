from aiogram import Dispatcher

from bot.middlewares.blocking import BlockingMiddleware
from bot.middlewares.throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher):
    dp.setup_middleware(
        BlockingMiddleware())
    dp.setup_middleware(
        ThrottlingMiddleware())


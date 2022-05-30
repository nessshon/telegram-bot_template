from typing import Union

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bot.config import config


def get_storage(redis: bool = False) -> Union[RedisStorage2, MemoryStorage]:
    return RedisStorage2(db=1) if redis else MemoryStorage()


storage = get_storage(redis=True)

bot = Bot(
    token=config.bot.TOKEN,
    parse_mode=types.ParseMode.HTML,
)
dp = Dispatcher(
    bot=bot,
    storage=storage,
)

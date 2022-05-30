from aiogram import Dispatcher

from bot.filters.is_group import IsGroup
from bot.filters.is_private import IsPrivate

from bot.filters.is_admin import IsAdmin
from bot.filters.is_moder import IsModer
from bot.filters.is_creator import IsCreator


def setup_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)

    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsModer)
    dp.filters_factory.bind(IsCreator)

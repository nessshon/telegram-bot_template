from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards.callback_data import cdata


async def callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.hide:
        with suppress(Exception):
            await call.message.delete()

    await call.answer()

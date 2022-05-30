from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from bot.database import db
from bot.keyboards.callback_data import cdata

from bot.handlers.users.functions.main import main
from bot.handlers.users.functions.sponsored import (get_sponsored,
                                                    edit_sponsored)


async def sponsored_callback_handler(call: CallbackQuery, state: FSMContext):
    sponsored_data = await get_sponsored()

    if call.data == cdata.check:
        if any(sponsored_data):
            text = await db.message.get_text(code='sponsored_info')

            await call.answer(text=text, show_alert=True)
            await edit_sponsored(
                call=call,
                sponsored_data=sponsored_data)

        else:
            await main(message=call.message, state=state)

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.database import db
from bot.handlers.admins.functions.buttons import (buttons_list,
                                                   buttons_send_text,
                                                   buttons_search)

from bot.handlers.admins.functions.main import main_admin
from bot.keyboards.callback_data import cdata


async def buttons_list_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.search:
        await buttons_search(message=call.message, state=state)

    else:
        buttons_data = await db.button.get_code_ru_all()

        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await buttons_list(call=call, state=state)

        elif call.data in list(buttons_data.keys()):
            await state.update_data(code=call.data)

            await buttons_send_text(state=state, message=call.message)

    await call.answer()

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.database import db
from bot.handlers.admins.functions.main import main_admin
from bot.handlers.admins.functions.messages import (messages_list,
                                                    messages_send_text,
                                                    messages_search)
from bot.keyboards.callback_data import cdata


async def messages_list_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.search:
        await messages_search(message=call.message, state=state)

    else:
        messages_data = await db.message.get_code_desc_all()

        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await messages_list(call=call, state=state)

        elif call.data in list(messages_data.keys()):
            await state.update_data(code=call.data)

            await messages_send_text(state=state, message=call.message)

    await call.answer()

from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery

from bot.database import db
from bot.handlers.admins.functions.main import main_admin

from bot.texts import texts
from bot.keyboards.callback_data import cdata

from bot.handlers.admins.functions.sponsorship import (sponsorship,
                                                       sponsorship_list,
                                                       sponsorship_choice,
                                                       sponsorship_edit_chat_id,
                                                       sponsorship_edit_chat_title,
                                                       sponsorship_delete,
                                                       sponsorship_send_chat_id)


async def sponsorship_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.list:
        sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

        if sponsorship_data:
            await sponsorship_list(call=call, state=state)

        else:
            text = texts.message.sponsorship_info

            await call.answer(text=text, show_alert=True)

    elif call.data == cdata.add:
        await sponsorship_send_chat_id(message=call.message, state=state)

    await call.answer()


async def sponsorship_list_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await sponsorship(state=state, call=call)

    else:
        sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await sponsorship_list(call=call, state=state)

        elif call.data in list(sponsorship_data.keys()):
            await state.update_data(chat_id=call.data)

            await sponsorship_choice(state=state, call=call)

    await call.answer()


async def sponsorship_choice_callback_handler(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    if call.data == cdata.back:
        await sponsorship_list(call=call, state=state)

    elif call.data in [cdata.sponsorship_inactive, cdata.sponsorship_active]:
        await db.sponsorship.update_status(chat_id=user_data['chat_id'], status=call.data)

        await sponsorship_choice(state=state, call=call)

    elif call.data == cdata.sponsorship_edit_chat_id:
        await sponsorship_edit_chat_id(message=call.message, state=state)

    elif call.data == cdata.sponsorship_edit_chat_title:
        await sponsorship_edit_chat_title(message=call.message, state=state)

    elif call.data == cdata.delete:
        await sponsorship_delete(message=call.message, state=state)

    await call.answer()

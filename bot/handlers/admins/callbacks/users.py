from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.config import config
from bot.database import db

from bot.handlers.admins.functions.main import main_admin
from bot.handlers.admins.functions.users import (users_search,
                                                 users_list,
                                                 users_choose, users_send_message)
from bot.keyboards.callback_data import cdata
from bot.texts import texts


async def users_list_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.search:
        await users_search(message=call.message, state=state)

    else:
        users_data = await db.user.get_user_id_first_name_all()

        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await users_list(call=call, state=state)

        elif call.data.isdigit() and int(call.data) in list(users_data.keys()):
            await state.update_data(user_id=int(call.data))

            await users_choose(state=state, message=call.message)

    await call.answer()


async def users_choose_callback_handler(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    if call.data == cdata.back:
        await users_list(state=state, message=call.message)

    elif call.data == cdata.block:
        if user_data['user_id'] == int(config.bot.CREATOR_ID):
            text = texts.message.users_not_blocked

            await call.answer(text=text, show_alert=True)

        elif call.from_user.id == user_data['user_id']:
            text = texts.message.users_not_blocked2

            await call.answer(text=text, show_alert=True)
        else:
            await db.user.block(user_id=user_data['user_id'])
            await users_choose(state=state, call=call)

    elif call.data == cdata.unblock:
        await db.user.block(user_id=user_data['user_id'], state='joined')
        await users_choose(state=state, call=call)

    elif call.data == cdata.send_message:
        await users_send_message(message=call.message, state=state)

    await call.answer()

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.database import db
from bot.handlers.admins.functions.paginator import Paginator
from bot.handlers.admins.functions.admins import (admins_add,
                                                  admins_add_confirm,
                                                  admins_status,
                                                  admins,
                                                  admins_list,
                                                  admins_first_name,
                                                  admins_choose,
                                                  admins_edit_name,
                                                  admins_edit_id)

from bot.handlers.admins.functions.main import main_admin
from bot.keyboards.callback_data import cdata
from bot.texts import texts
from bot.utils.bot import commands
from bot.utils.bot.message import send_auto_delete_message


async def admins_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.list:
        if await db.admin.get_user_id_all():
            await admins_list(call=call, state=state)
        else:
            text = texts.message.admins_list_info
            await call.answer(text=text, show_alert=True)

    elif call.data == cdata.add:
        await admins_add(message=call.message, state=state)

    await call.answer()


async def admins_status_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await admins_first_name(message=call.message, state=state)

    elif call.data in [cdata.admin, cdata.moder]:
        await state.update_data(status=call.data)

        await admins_add_confirm(call=call, state=state)

    await call.answer()


async def admins_add_confirm_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await admins_status(call=call, state=state)

    elif call.data == cdata.confirm:
        user_data = await state.get_data()
        await db.admin.add(
            role=user_data['status'],
            user_id=user_data['admin_id'],
            first_name=user_data['admin_name'])

        await admins(call=call, state=state)

        text = texts.message.admins_added.format(url=user_data['url'])
        await send_auto_delete_message(message=call.message, text=text)
        await commands.setup()

    await call.answer()


async def admins_list_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await admins(state=state, call=call)

    elif call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
        admins_data = await db.admin.get_user_id_first_name_all()
        text_list, callback_data_list = list(admins_data.values()), list(admins_data.keys())

        paginator = Paginator(
            text_list=text_list,
            callback_data_list=callback_data_list)
        await paginator.edit_reply_markup(call=call, state=state)

    elif call.data.isdigit() and int(call.data) in await db.admin.get_user_id_all():
        await state.update_data(admin_id=int(call.data))
        await admins_choose(state=state, message=call.message)

    await call.answer()


async def admins_choose_callback_handler(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    if call.data == cdata.back:
        await admins_list(state=state, message=call.message)

    elif call.data == cdata.switch_to_admin:
        await db.admin.update_role_admin(user_id=user_data['admin_id'])
        await admins_choose(state=state, call=call)

    elif call.data == cdata.switch_to_moder:
        await db.admin.update_role_moder(user_id=user_data['admin_id'])
        await admins_choose(state=state, call=call)

    elif call.data == cdata.switch_to_user:
        await db.admin.delete(user_id=user_data['admin_id'])
        await admins(state=state, message=call.message)

    elif call.data == cdata.edit_name:
        await admins_edit_name(message=call.message, state=state)

    elif call.data == cdata.edit_id:
        await admins_edit_id(message=call.message, state=state)

    await call.answer()

from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import BadRequest

from bot.handlers.admins.functions.paginator import Paginator
from bot.handlers.admins.functions.main import main_admin
from bot.handlers.admins.functions.newsletter import (newsletter_create,
                                                      newsletter_run_or_postpone,
                                                      newsletter_run_confirm,
                                                      newsletter_postpone,
                                                      newsletter_postponed,
                                                      newsletter,
                                                      newsletter_choose,
                                                      newsletter_edit_time,
                                                      newsletter_delete)
from bot.scheduler.loader import scheduler

from bot.texts import texts
from bot.keyboards.callback_data import cdata
from bot.utils.bot.message import send_auto_delete_message


async def newsletter_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.create:
        await newsletter_create(message=call.message, state=state)

    elif call.data == cdata.postponed:
        if scheduler.get_jobs():
            await newsletter_postponed(call=call, state=state)

        else:
            text = texts.message.newsletter_postponed_info

            await call.answer(text=text, show_alert=True)

    await call.answer()


async def newsletter_run_or_postpone_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await newsletter_create(message=call.message, state=state)

    elif call.data == cdata.run:
        await newsletter_run_confirm(message=call.message, state=state)

    elif call.data == cdata.postpone:
        await newsletter_postpone(message=call.message, state=state)

    await call.answer()


async def newsletter_postponed_callback_handler(call: CallbackQuery, state: FSMContext):
    btn_list = [str(i)[:-9] for i in [i.next_run_time for i in scheduler.get_jobs()]]

    if call.data == cdata.back:
        async with state.proxy() as data:
            data.pop('curr_page')
        await newsletter(call=call, state=state)

    elif call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
        paginator = Paginator(
            text_list=btn_list,
            callback_data_list=btn_list)
        await paginator.edit_reply_markup(call=call, state=state)

    elif call.data in btn_list:
        await state.update_data(job_id=call.data)
        await newsletter_choose(call=call, state=state)

    await call.answer()


async def newsletter_choose_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        try:
            await newsletter_postponed(state=state, call=call)
        except BadRequest:
            await newsletter_postponed(state=state, message=call.message)

    elif call.data == cdata.edit_time:
        await newsletter_edit_time(message=call.message, state=state)

    elif call.data == cdata.del_post:
        try:
            await newsletter_delete(call=call, state=state)
        except BadRequest:
            await newsletter_delete(message=call.message, state=state)

    await call.answer()


async def newsletter_delete_callback_handler(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    if call.data == cdata.back:
        await newsletter_choose(state=state, call=call)

    elif call.data == cdata.confirm:
        scheduler.remove_job(job_id=user_data['job_id'])
        await newsletter(state=state, call=call)

        text = texts.message.newsletter_deleted
        await send_auto_delete_message(message=call.message, text=text)

    await call.answer()

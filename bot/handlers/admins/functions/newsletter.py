from contextlib import suppress
from datetime import datetime

from aiogram.dispatcher import FSMContext

from aiogram.types import (Message,
                           CallbackQuery)


from bot.loader import bot
from bot.scheduler.loader import scheduler

from bot.texts import texts
from bot.states import states
from bot.keyboards import keyboards

from bot.utils.bot.message import (edit_message,
                                   delete_message)

from bot.handlers.admins.functions.paginator import Paginator


async def newsletter(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.newsletter.set()

    text = texts.message.newsletter
    markup = await keyboards.inline.newsletter()

    if call:
        await edit_message(
            call=call,
            text=text,
            reply_markup=markup)

    if message:
        msg = await message.answer(
            text=text,
            reply_markup=markup)

        await delete_message(message_id2=True)
        await state.update_data(message_id=msg.message_id)


async def newsletter_create(message: Message, state: FSMContext):
    await states.admin.newsletter_create.set()
    user_data = await state.get_data()

    if 'newsletter_type' in user_data:
        markup = None if 'newsletter_buttons' not in user_data else \
            await keyboards.inline.newsletter_buttons(buttons=user_data['newsletter_buttons'])

        if user_data['newsletter_type'] == 'photo':
            photo = user_data['newsletter_photo']
            caption = user_data['newsletter_caption']

            msg2 = await message.answer_photo(
                photo=photo,
                caption=caption,
                reply_markup=markup)

        elif user_data['newsletter_type'] == 'text':
            text = user_data['newsletter_text']

            msg2 = await message.answer(
                text=text,
                reply_markup=markup)

    text = texts.message.newsletter_create
    markup = await keyboards.reply.newsletter_create(user_data=user_data)

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message(message_id2=True)
    await state.update_data(message_id=msg.message_id)

    if 'newsletter_type' in user_data:
        await state.update_data(message_id2=msg2.message_id)


async def newsletter_add_buttons(message: Message, state: FSMContext):
    await states.admin.newsletter_add_buttons.set()

    text = texts.message.newsletter_add_buttons
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message(message_id2=True)
    await state.update_data(message_id=msg.message_id)


async def newsletter_run_or_postpone(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.newsletter_run_or_postpone.set()

    text = texts.message.newsletter_run_or_postpone
    markup = await keyboards.inline.newsletter_run_or_postpone()

    if call:
        await edit_message(
            call=call,
            text=text,
            reply_markup=markup)

    if message:
        msg = await message.answer(
            text=text,
            reply_markup=markup)
        await delete_message(message_id2=True)
        await state.update_data(message_id=msg.message_id)


async def newsletter_run_confirm(message: Message, state: FSMContext):
    await states.admin.newsletter_run_confirm.set()

    user_data = await state.get_data()

    markup = None if 'newsletter_buttons' not in user_data else \
        await keyboards.inline.newsletter_buttons(buttons=user_data['newsletter_buttons'])

    if user_data['newsletter_type'] == 'photo':
        photo = user_data['newsletter_photo']
        caption = user_data['newsletter_caption']

        msg2 = await message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=markup)

    if user_data['newsletter_type'] == 'text':
        text = user_data['newsletter_text']

        msg2 = await message.answer(
            text=text,
            reply_markup=markup)

    text = texts.message.newsletter_run_confirm
    markup = await keyboards.reply.confirm_back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message(message_id2=True)
    await state.update_data(
        message_id=msg.message_id,
        message_id2=msg2.message_id)


async def newsletter_postpone(message: Message, state: FSMContext):
    await states.admin.newsletter_postpone.set()

    datetime_a = datetime.now().strftime('%H %M %d %m %Y')
    datetime_b = datetime.now().strftime("%H:%M %-d %b %Y г")

    text = texts.message.newsletter_date_time.format(
        datetime_a=datetime_a,
        datetime_b=datetime_b)
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def newsletter_postponed(state: FSMContext, call: CallbackQuery = None, message: Message = None):
    await states.admin.newsletter_postponed.set()

    btn_list = [str(i)[:-9] for i in [i.next_run_time for i in scheduler.get_jobs()]]

    text = texts.message.newsletter_postponed
    paginator = Paginator(
        text_list=btn_list,
        callback_data_list=btn_list)

    if call:
        await paginator.edit_text(call=call, state=state, text=text)

    if message:
        await paginator.send_message(message=message, state=state, text=text)


async def newsletter_choose(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.newsletter_choose.set()
    user_data = await state.get_data()

    data_job = scheduler.get_job(job_id=user_data['job_id']).args[0]
    buttons = dict() if 'newsletter_buttons' not in data_job else data_job['newsletter_buttons']
    markup = await keyboards.inline.newsletter_choose(buttons=buttons)

    if data_job['newsletter_type'] == 'text':
        text = data_job['newsletter_text']

        if call:
            with suppress(Exception):
                await call.message.edit_text(
                    text=text,
                    reply_markup=markup)
        elif message:
            msg = await message.answer(
                text=text,
                reply_markup=markup)
            await delete_message()
            await state.update_data(message_id=msg.message_id)

    elif data_job['newsletter_type'] == 'photo':
        photo = data_job['newsletter_photo']
        caption = data_job['newsletter_caption']

        if call:
            with suppress(Exception):
                msg = await call.message.answer_photo(
                    photo=photo,
                    caption=caption,
                    reply_markup=markup)

        elif message:
            msg = await message.answer_photo(
                photo=photo,
                caption=caption,
                reply_markup=markup)
        await delete_message()
        await state.update_data(message_id=msg.message_id)


async def newsletter_edit_time(message: Message, state: FSMContext):
    await states.admin.newsletter_edit_time.set()

    datetime_a = datetime.now().strftime('%H %M %d %m %Y')
    datetime_b = datetime.now().strftime("%H:%M %-d %b %Y г")

    text = texts.message.newsletter_date_time.format(
        datetime_a=datetime_a,
        datetime_b=datetime_b)
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def newsletter_delete(state: FSMContext, call: CallbackQuery = None, message: Message = None):
    await states.admin.newsletter_delete.set()

    text = texts.message.newsletter_delete
    markup = await keyboards.inline.back_confirm()

    if call:
        await edit_message(
            call=call,
            text=text,
            reply_markup=markup)

    if message:
        msg = await message.answer(
            text=text,
            reply_markup=markup)
        await delete_message()
        await state.update_data(message_id=msg.message_id)

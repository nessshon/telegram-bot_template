from aiogram.dispatcher import FSMContext

from aiogram.types import (Message,
                           CallbackQuery)

from aiogram.utils.exceptions import ChatNotFound
from aiogram.utils.markdown import hcode

from bot.loader import bot
from bot.database import db

from bot.texts import texts
from bot.states import states
from bot.keyboards import keyboards
from bot.keyboards.callback_data import cdata

from bot.utils.bot.message import (edit_message,
                                   delete_message)

from bot.handlers.admins.functions.paginator import Paginator


async def sponsorship(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.sponsorship.set()

    text = texts.message.sponsorship
    markup = await keyboards.inline.list_add()

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


async def sponsorship_list(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.sponsorship_list.set()

    sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

    text = texts.message.sponsorship_list
    text_list, callback_data_list = list(sponsorship_data.values()), list(sponsorship_data.keys())

    paginator = Paginator(
        text_list=text_list,
        callback_data_list=callback_data_list)

    if message:
        await paginator.send_message(message=message, state=state, text=text)

    if call:
        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await paginator.edit_reply_markup(call=call, state=state)

        else:
            await paginator.edit_text(call=call, state=state, text=text)


async def sponsorship_choice(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.sponsorship_choice.set()
    user_data = await state.get_data()

    chat_id = user_data['chat_id']
    chat = await db.sponsorship.get(chat_id=chat_id)
    chat_title = chat.chat_title
    status = chat.status

    status_t = texts.button.sponsorship_active_t if chat.status == cdata.sponsorship_active \
        else texts.button.sponsorship_inactive_t

    try:
        get_chat = await bot.get_chat(chat_id=chat_id)
        chat_url = await get_chat.get_url()
    except ChatNotFound:
        chat_url = texts.message.sponsorship_chat_not_found.replace('\n\n', '\n')

    text = texts.message.sponsorship_choice.format(
        chat_id=chat_id,
        chat_title=chat_title,
        status=status_t,
        chat_url=chat_url)
    markup = await keyboards.inline.sponsorship_choice(status=status)

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


async def sponsorship_edit_chat_id(message: Message, state: FSMContext):
    await states.admin.sponsorship_edit_chat_id.set()

    user_data = await state.get_data()

    text = texts.message.sponsorship_edit_chat_id.format(chat_id=user_data['chat_id'])
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def sponsorship_edit_chat_title(message: Message, state: FSMContext):
    await states.admin.sponsorship_edit_chat_title.set()

    user_data = await state.get_data()
    chat_title = await db.sponsorship.get_chat_title(chat_id=user_data['chat_id'])

    text = texts.message.sponsorship_edit_chat_title.format(chat_title=hcode(chat_title))
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def sponsorship_delete(message: Message, state: FSMContext):
    await states.admin.sponsorship_delete.set()

    user_data = await state.get_data()
    chat_id = user_data['chat_id']
    chat = await db.sponsorship.get(chat_id=user_data['chat_id'])
    chat_title = chat.chat_title

    try:
        get_chat = await bot.get_chat(chat_id=chat_id)
        chat_url = await get_chat.get_url()
    except ChatNotFound:
        chat_url = texts.message.sponsorship_chat_not_found.replace('\n\n', '\n')

    text = texts.message.sponsorship_delete.format(
        chat_title=chat_title,
        chat_id=chat_id,
        chat_url=chat_url)
    markup = await keyboards.reply.confirm_back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def sponsorship_send_chat_id(message: Message, state: FSMContext):
    await states.admin.sponsorship_send_chat_id.set()

    text = texts.message.sponsorship_send_chat_id
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def sponsorship_send_chat_title(message: Message, state: FSMContext):
    await states.admin.sponsorship_send_chat_title.set()

    text = texts.message.sponsorship_send_chat_title
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def sponsorship_add(message: Message, state: FSMContext):
    await states.admin.sponsorship_add.set()

    user_data = await state.get_data()
    chat_id = user_data['chat_id']
    chat_title = user_data['chat_title']

    try:
        get_chat = await bot.get_chat(chat_id=chat_id)
        chat_url = await get_chat.get_url()
    except ChatNotFound:
        chat_url = texts.message.sponsorship_chat_not_found.replace('\n\n', '\n')

    text = texts.message.sponsorship_add.format(
        chat_title=chat_title,
        chat_id=chat_id,
        chat_url=chat_url)
    markup = await keyboards.reply.confirm_back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)

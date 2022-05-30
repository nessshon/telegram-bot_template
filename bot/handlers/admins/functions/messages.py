from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hcode

from bot.database import db
from bot.handlers.admins.functions.paginator import Paginator
from bot.keyboards import keyboards
from bot.keyboards.callback_data import cdata
from bot.states import states
from bot.texts import texts
from bot.utils.bot.message import edit_message, delete_message


async def messages(message: Message, state: FSMContext):
    await messages_list(state=state, message=message)


async def messages_list(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.messages_list.set()
    user_data = await state.get_data()

    messages_data = await db.message.get_code_desc_all() if 'text_filter' not in user_data \
        else await db.message.get_code_desc_filer_all(text=user_data['text_filter'])

    text_list, callback_data_list = list(messages_data.values()), list(messages_data.keys())

    text = texts.message.messages_list if 'text_filter' not in user_data \
        else texts.message.messages_find.format(count=len(text_list))

    paginator = Paginator(
        text_list=text_list,
        callback_data_list=callback_data_list)

    if message:
        await paginator.send_message(message=message, state=state, text=text, search=True)

    if call:
        if call.data in [cdata.first_page, cdata.prev_page, cdata.curr_page, cdata.next_page, cdata.last_page]:
            await paginator.edit_reply_markup(call=call, state=state, search=True)

        else:
            await paginator.edit_text(call=call, state=state, text=text, search=True)


async def messages_send_text(message: Message, state: FSMContext):
    await states.admin.messages_send_text.set()

    user_data = await state.get_data()
    text_original = await db.message.get_text(
        code=user_data['code'])
    text = texts.message.messages_send_text.format(text_original=hcode(text_original))
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def messages_confirm(message: Message, state: FSMContext):
    await states.admin.messages_confirm.set()

    user_data = await state.get_data()
    text_new = user_data['text']
    text_original = await db.message.get_text(
        code=user_data['code'])
    text = texts.message.messages_confirm.format(
        text_original=text_original,
        text_new=text_new)
    markup = await keyboards.reply.confirm_back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def messages_search(message: Message, state: FSMContext):
    await states.admin.messages_search.set()

    text = texts.message.messages_search
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)

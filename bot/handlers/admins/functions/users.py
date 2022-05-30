from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InputFile

from bot.data import BASE_DIR
from bot.database import db
from bot.handlers.admins.functions.paginator import Paginator
from bot.keyboards import keyboards
from bot.keyboards.callback_data import cdata
from bot.loader import bot
from bot.states import states
from bot.texts import texts
from bot.utils.bot.message import delete_message


async def users(message: Message, state: FSMContext):
    await users_list(state=state, message=message)


async def users_list(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.users_list.set()
    user_data = await state.get_data()

    users_data = await db.user.get_user_id_first_name_all() if 'text_filter' not in user_data \
        else await db.user.get_user_id_first_name_filter_all(text=user_data['text_filter'])

    text_list, callback_data_list = list(users_data.values()), list(users_data.keys())

    text = texts.message.users_list if 'text_filter' not in user_data \
        else texts.message.users_find.format(count=len(text_list))

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


async def users_choose(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.users_choose.set()
    user_data = await state.get_data()

    user = await db.user.get(user_id=user_data['user_id'])

    user_state = texts.button.__getattribute__(user.state)

    text = texts.message.users_choose.format(
        url=f'<a href="tg://user?id={user.user_id}">{user.first_name}</a>',
        state=user_state,
        user_id=user.user_id,
        created_at=user.created_at.strftime("%H:%M %Y-%m-%d"))
    markup = await keyboards.inline.users_choose(user_state=user.state)

    path_photo = BASE_DIR / 'photo/no_photo.png'
    user_photo = await bot.get_user_profile_photos(user_id=user.user_id, offset=0)
    photo = user_photo.photos[0][-1].file_id if any(user_photo.photos) else InputFile(path_or_bytesio=path_photo)

    if call:
        with suppress(Exception):
            await call.message.edit_caption(
                caption=text,
                reply_markup=markup)

    if message:
        msg = await message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=markup)
        await delete_message(message_id2=True)
        await state.update_data(message_id=msg.message_id)


async def users_search(message: Message, state: FSMContext):
    await states.admin.users_search.set()

    text = texts.message.users_search
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def users_send_message(message: Message, state: FSMContext):
    await states.admin.users_send_message.set()

    text = texts.message.users_send_message
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message(message_id2=True)
    await state.update_data(message_id=msg.message_id)


async def users_send_message_confirm(message: Message, state: FSMContext):
    await states.admin.users_send_message_confirm.set()
    user_data = await state.get_data()

    if user_data['message_type'] == 'photo':
        photo = user_data['message_photo']
        caption = user_data['message_caption']

        msg2 = await message.answer_photo(
            photo=photo,
            caption=caption)
    if user_data['message_type'] == 'text':
        text = user_data['message_text']

        msg2 = await message.answer(text=text)

    text = texts.message.users_send_message_confirm
    markup = await keyboards.reply.confirm_back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message(message_id2=True)
    await state.update_data(message_id=msg.message_id)
    if 'message_type' in user_data:
        await state.update_data(message_id2=msg2.message_id)

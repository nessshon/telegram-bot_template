from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InputFile

from bot.data import BASE_DIR
from bot.database import db
from bot.handlers.admins.functions.paginator import Paginator
from bot.keyboards import keyboards
from bot.keyboards.callback_data import cdata
from bot.loader import bot
from bot.states import states
from bot.texts import texts
from bot.utils.bot.message import edit_message, delete_message


async def admins(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.admins.set()

    text = texts.message.admins
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


async def admins_add(message: Message, state: FSMContext):
    await states.admin.admins_add.set()

    text = texts.message.admins_add
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def admins_first_name(message: Message, state: FSMContext):
    await states.admin.admins_first_name.set()

    text = texts.message.admins_first_name
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def admins_status(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.admins_status.set()

    text = texts.message.admins_status
    markup = await keyboards.inline.admins_status()

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


async def admins_add_confirm(call: CallbackQuery, state: FSMContext):
    await states.admin.admins_add_confirm.set()
    user_data = await state.get_data()

    admin_id = user_data['admin_id']
    admin_name = user_data['admin_name']
    status = texts.button.admin if user_data['status'] == cdata.admin else texts.button.moder
    url = f'<a href="tg://user?id={user_data["admin_id"]}">{admin_name}</a>'

    text = texts.message.admins_add_confirm.format(
        url=url,
        user_id=admin_id,
        status=status)
    markup = await keyboards.inline.back_confirm()

    await edit_message(
        call=call,
        text=text,
        reply_markup=markup)
    await state.update_data(url=url)


async def admins_list(state: FSMContext, message: Message = None, call: CallbackQuery = None):
    await states.admin.admins_list.set()

    text = texts.message.admins_list
    admins_data = await db.admin.get_user_id_first_name_all()
    text_list, callback_data_list = list(admins_data.values()), list(admins_data.keys())

    paginator = Paginator(
        text_list=text_list,
        callback_data_list=callback_data_list)

    if call:
        await paginator.edit_text(call=call, state=state, text=text)

    if message:
        await paginator.send_message(message=message, state=state, text=text)


async def admins_choose(state: FSMContext, call: CallbackQuery = None, message: Message = None):
    await states.admin.admins_choose.set()

    user_data = await state.get_data()

    admin = await db.admin.get(user_id=user_data['admin_id'])
    status = texts.button.admin if admin.role == cdata.admin else texts.button.moder
    url = f'<a href="tg://user?id={admin.user_id}">{admin.first_name}</a>'

    text = texts.message.admins_choose.format(
        url=url,
        user_id=admin.user_id,
        status=status)
    markup = await keyboards.inline.admins_choose(status=admin.role)

    path_photo = BASE_DIR / 'photo/no_photo.png'
    user_photo = await bot.get_user_profile_photos(user_id=user_data['admin_id'], offset=0)
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
        await delete_message()
        await state.update_data(message_id=msg.message_id)


async def admins_edit_name(message: Message, state: FSMContext):
    await states.admin.admins_edit_name.set()

    text = texts.message.admins_edit_name
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def admins_edit_id(message: Message, state: FSMContext):
    await states.admin.admins_edit_id.set()

    text = texts.message.admins_edit_id
    markup = await keyboards.reply.back()

    msg = await message.answer(
        text=text,
        reply_markup=markup)
    await delete_message()
    await state.update_data(message_id=msg.message_id)

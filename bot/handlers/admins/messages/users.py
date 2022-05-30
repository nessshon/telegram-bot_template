from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import BotBlocked

from bot.database import db

from bot.handlers.admins.functions.users import users_choose, users_list, users_send_message_confirm, users_send_message
from bot.loader import bot

from bot.texts import texts
from bot.utils.bot.message import delete_message, send_auto_delete_message


async def users_list_message_handler(message: Message):
    await delete_message(message=message)


async def users_choose_message_handler(message: Message):
    await delete_message(message=message)


async def users_search_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            async with state.proxy() as data:
                if 'text_filter' in data:
                    data.pop('text_filter')
            await users_choose(message=message, state=state)
        else:
            users_data = await db.user.get_user_id_first_name_filter_all(text=message.text)
            if any(users_data):
                await state.update_data(text_filter=message.text)
                await users_list(state=state, message=message)

            else:
                text = texts.message.users_not_find
                await send_auto_delete_message(message=message, text=text)

    await delete_message(message=message)


async def users_send_message_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await users_choose(state=state, message=message)
        else:
            await state.update_data(
                message_type='text',
                message_text=message.parse_entities())
            await users_send_message_confirm(message=message, state=state)

    elif message.content_type == 'photo':
        caption = None if not message.caption else message.parse_entities()

        await state.update_data(
            message_type='photo',
            message_photo=message.photo[-1].file_id,
            message_caption=caption)
        await users_send_message_confirm(message=message, state=state)

    await delete_message(message=message)


async def users_send_message_confirm_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await users_send_message(message=message, state=state)

        elif message.text == texts.button.confirm:
            await users_choose(state=state, message=message)

            if user_data['message_type'] == 'text':
                try:
                    text = user_data['message_text']

                    await bot.send_message(
                        chat_id=user_data['user_id'],
                        text=text)
                    name = await db.user.get_first_name(user_id=user_data['user_id'])

                    url = f'<a href="tg://user?id={user_data["user_id"]}">{name}</a>'
                    text = texts.message.users_message_sent.format(url=url)

                    await send_auto_delete_message(message=message, text=text)

                except BotBlocked:
                    text = texts.message.users_send_message_err
                    await send_auto_delete_message(message=message, text=text)

            if user_data['message_type'] == 'photo':
                photo = user_data['message_photo']
                caption = user_data['message_caption']

                try:
                    await bot.send_photo(
                        chat_id=user_data['user_id'],
                        photo=photo,
                        caption=caption)
                    name = await db.user.get_first_name(user_id=user_data['user_id'])

                    url = f'<a href="tg://user?id={user_data["user_id"]}">{name}</a>'
                    text = texts.message.users_message_sent.format(url=url)

                    await send_auto_delete_message(message=message, text=text)

                except BotBlocked:
                    text = texts.message.users_send_message_err
                    await send_auto_delete_message(message=message, text=text)

    await delete_message(message=message)

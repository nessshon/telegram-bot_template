from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.database import db
from bot.handlers.admins.functions.buttons import (buttons_list,
                                                   buttons_confirm,
                                                   buttons_send_text)
from bot.keyboards import keyboards

from bot.texts import texts
from bot.utils.bot.message import delete_message, send_auto_delete_message


async def buttons_list_message_handler(message: Message):
    await delete_message(message=message)


async def buttons_send_text_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await buttons_list(state=state, message=message)
        else:
            await state.update_data(text=message.text)

            await buttons_confirm(message=message, state=state)

    await delete_message(message=message)


async def buttons_confirm_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await buttons_send_text(message=message, state=state)

        elif message.text == texts.button.confirm:
            await db.button.update(
                code=user_data['code'],
                text=user_data['text'])
            await buttons_list(state=state, message=message)

            text = texts.message.buttons_edited
            await send_auto_delete_message(message=message, text=text, time=5)

    await delete_message(message=message)


async def buttons_search_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            async with state.proxy() as data:
                if 'text_filter' in data:
                    data.pop('text_filter')
            await buttons_list(state=state, message=message)

        else:
            buttons_data = await db.button.get_code_ru_filer_all(text=message.text)
            if any(buttons_data):
                await state.update_data(text_filter=message.text)

                await buttons_list(state=state, message=message)

            else:
                text = texts.message.buttons_not_find
                markup = await keyboards.reply.back()

                msg = await message.answer(text=text, reply_markup=markup)
                await delete_message()
                await state.update_data(message_id=msg.message_id)

    await delete_message(message=message)

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.database import db
from bot.handlers.admins.functions.messages import (messages_list,
                                                    messages_confirm,
                                                    messages_send_text)
from bot.keyboards import keyboards

from bot.texts import texts
from bot.utils.bot.message import delete_message, send_auto_delete_message


async def messages_list_message_handler(message: Message):
    await delete_message(message=message)


async def messages_send_text_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await messages_list(state=state, message=message)
        else:
            await state.update_data(text=message.text)

            await messages_confirm(message=message, state=state)

    await delete_message(message=message)


async def messages_confirm_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await messages_send_text(message=message, state=state)

        elif message.text == texts.button.confirm:
            await db.message.update(
                code=user_data['code'],
                text=user_data['text'])
            await messages_list(state=state, message=message)

            text = texts.message.messages_edited
            await send_auto_delete_message(message=message, text=text, time=5)

    await delete_message(message=message)


async def messages_search_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            async with state.proxy() as data:
                if 'text_filter' in data:
                    data.pop('text_filter')
            await messages_list(state=state, message=message)

        else:
            messages_data = await db.message.get_code_desc_filer_all(text=message.text)
            if any(messages_data):
                await state.update_data(text_filter=message.text)

                await messages_list(state=state, message=message)

            else:
                text = texts.message.messages_not_find
                markup = await keyboards.reply.back()

                msg = await message.answer(text=text, reply_markup=markup)
                await delete_message()
                await state.update_data(message_id=msg.message_id)

    await delete_message(message=message)

from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from aiogram.utils.exceptions import ChatNotFound

from bot.loader import bot
from bot.database import db

from bot.handlers.admins.functions.sponsorship import (sponsorship,
                                                       sponsorship_choice,
                                                       sponsorship_list,
                                                       sponsorship_send_chat_id,
                                                       sponsorship_send_chat_title,
                                                       sponsorship_add)

from bot.texts import texts
from bot.keyboards import keyboards

from bot.utils.bot.message import delete_message, send_auto_delete_message


async def sponsorship_message_handler(message: Message):
    await delete_message(message=message)


async def sponsorship_list_message_handler(message: Message):
    await delete_message(message=message)


async def sponsorship_edit_choice_message_handler(message: Message):
    await delete_message(message=message)


async def sponsorship_edit_chat_id_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship_choice(state=state, message=message)

        else:
            try:
                await bot.get_chat(chat_id=message.text)
                sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

                if any(sponsorship_data) and message.text in list(
                        (await db.sponsorship.get_chat_id_chat_title_all()).keys()):
                    text = texts.message.sponsorship_chat_exists
                    markup = await keyboards.reply.back()

                    msg = await message.answer(
                        text=text,
                        reply_markup=markup)

                    await delete_message()
                    await state.update_data(message_id=msg.message_id)

                else:
                    await db.sponsorship.update_chat_id(chat_id=user_data['chat_id'], new_chat_id=message.text)
                    await state.update_data(chat_id=message.text)
                    await sponsorship_choice(state=state, message=message)

                    text = texts.message.sponsorship_edited_chat_id
                    await send_auto_delete_message(message=message, text=text, time=5)

            except ChatNotFound:
                text = texts.message.sponsorship_chat_not_found
                markup = await keyboards.reply.back()

                msg = await message.answer(
                    text=text,
                    reply_markup=markup)
                await delete_message()
                await state.update_data(message_id=msg.message_id)

    await delete_message(message=message)


async def sponsorship_edit_chat_title_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship_choice(state=state, message=message)

        else:
            await db.sponsorship.update_chat_title(chat_id=user_data['chat_id'], chat_title=message.text)
            await sponsorship_choice(state=state, message=message)

            text = texts.message.sponsorship_edited_chat_title
            await send_auto_delete_message(message=message, text=text, time=5)
    await delete_message(message=message)


async def sponsorship_delete_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship_choice(state=state, message=message)

        elif message.text == texts.button.confirm:
            await db.sponsorship.delete(chat_id=user_data['chat_id'])
            sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

            if any(sponsorship_data):
                await sponsorship_list(state=state, message=message)
            else:
                await sponsorship(state=state, message=message)

            text = texts.message.sponsorship_deleted
            await send_auto_delete_message(message=message, text=text, time=5)

    await delete_message(message=message)


async def sponsorship_send_chat_id_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship(state=state, message=message)

        else:
            try:
                await bot.get_chat(chat_id=message.text)
                sponsorship_data = await db.sponsorship.get_chat_id_chat_title_all()

                if any(sponsorship_data) and message.text in list(
                        (await db.sponsorship.get_chat_id_chat_title_all()).keys()):
                    text = texts.message.sponsorship_chat_exists
                    markup = await keyboards.reply.back()

                    msg = await message.answer(
                        text=text,
                        reply_markup=markup)

                    await delete_message()
                    await state.update_data(message_id=msg.message_id)

                else:
                    await state.update_data(chat_id=message.text)

                    await sponsorship_send_chat_title(message=message, state=state)

            except ChatNotFound:
                text = texts.message.sponsorship_chat_not_found
                markup = await keyboards.reply.back()

                msg = await message.answer(
                    text=text,
                    reply_markup=markup)

                await delete_message()
                await state.update_data(message_id=msg.message_id)

    await delete_message(message=message)


async def sponsorship_send_chat_title_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship_send_chat_id(message=message, state=state)

        else:
            await state.update_data(chat_title=message.text)

            await sponsorship_add(message=message, state=state)

    await delete_message(message=message)


async def sponsorship_add_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await sponsorship_send_chat_title(message=message, state=state)

        elif message.text == texts.button.confirm:
            chat_id = user_data['chat_id']
            chat_title = user_data['chat_title']
            status = 'active'

            await db.sponsorship.add(
                status=status,
                chat_id=chat_id,
                chat_title=chat_title)
            await sponsorship(message=message, state=state)

            text = texts.message.sponsorship_added
            await send_auto_delete_message(message=message, text=text, time=5)

    await delete_message(message=message)

import asyncio
from contextlib import suppress

from aiogram.types import (User,
                           Message,
                           CallbackQuery,
                           InlineKeyboardMarkup)

from bot.loader import bot, dp

from aiogram.utils.exceptions import (MessageNotModified,
                                      MessageCantBeEdited,
                                      MessageToEditNotFound,
                                      MessageCantBeDeleted,
                                      MessageToDeleteNotFound)


async def send_auto_delete_message(message: Message, text: str, time: int = 3):
    msg = await message.answer(text=text)

    with suppress(MessageToDeleteNotFound):
        await asyncio.sleep(time)
        await msg.delete()


async def edit_message(call: CallbackQuery, text: str, reply_markup: InlineKeyboardMarkup):
    with suppress(MessageNotModified, MessageCantBeEdited, MessageToEditNotFound):
        await call.message.edit_text(
            text=text, reply_markup=reply_markup)


async def delete_message(message: Message = None, message_id2: bool = False):
    user = User.get_current()
    state = dp.current_state()

    with suppress(KeyError, MessageCantBeDeleted, MessageToDeleteNotFound):
        if message:
            message_id = message.message_id

            await bot.delete_message(
                chat_id=user.id,
                message_id=message_id)

        else:
            data = await state.get_data()

            message_id = data['message_id']

            await bot.delete_message(
                chat_id=user.id,
                message_id=message_id)

            if message_id2:
                await bot.delete_message(
                    chat_id=user.id,
                    message_id=data['message_id2'])

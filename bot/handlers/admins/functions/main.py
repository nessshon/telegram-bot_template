from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, User

from bot.keyboards import keyboards
from bot.states import states
from bot.texts import texts
from bot.utils.bot.message import delete_message, edit_message


async def main_admin(state: FSMContext, call: CallbackQuery = None, message: Message = None):
    user_id = User.get_current().id

    text = texts.message.main_admin
    markup = await keyboards.inline.main_admin(user_id=user_id)

    if call:
        with suppress(Exception):
            msg = await call.message.edit_text(
                text=text,
                reply_markup=markup)
            async with state.proxy() as data:
                data.clear()
            await states.admin.main.set()
            await state.update_data(message_id=msg.message_id)

    if message:
        msg = await message.answer(
            text=text,
            reply_markup=markup)
        await delete_message(message_id2=True)
        async with state.proxy() as data:
            data.clear()
        await states.admin.main.set()
        await state.update_data(message_id=msg.message_id)


async def reload_bot(call: CallbackQuery):
    await states.admin.reload_bot.set()

    text = texts.message.reload_bot
    markup = await keyboards.inline.back_confirm()

    await edit_message(
        call=call,
        text=text,
        reply_markup=markup)


async def stop_bot(call: CallbackQuery):
    await states.admin.stop_bot.set()

    text = texts.message.stop_bot
    markup = await keyboards.inline.back_confirm()

    await edit_message(
        call=call,
        text=text,
        reply_markup=markup)

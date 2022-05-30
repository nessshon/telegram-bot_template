from contextlib import suppress

from aiogram.types import (User,
                           Message,
                           CallbackQuery)

from aiogram.dispatcher import FSMContext

from aiogram.utils.exceptions import (BotBlocked,
                                      ChatNotFound)

from bot.loader import bot
from bot.database import db
from bot.config import config

from bot.texts import texts
from bot.states import states
from bot.keyboards import keyboards

from bot.utils.bot.message import (edit_message,
                                   delete_message)


async def sponsored(message: Message, state: FSMContext, sponsored_data):
    await states.user.sponsored.set()

    text = await db.message.get_text(code='sponsored')
    markup = await keyboards.inline.sponsored(sponsored_data=sponsored_data)

    msg = await message.answer(
        text=text,
        reply_markup=markup)

    await delete_message()
    await state.update_data(message_id=msg.message_id)


async def edit_sponsored(call: CallbackQuery, sponsored_data):
    await states.user.sponsored.set()

    text = await db.message.get_text(code='sponsored')
    markup = await keyboards.inline.sponsored(sponsored_data=sponsored_data)

    await edit_message(
        call=call,
        text=text,
        reply_markup=markup)


async def get_sponsored():
    sponsored_data = await db.sponsorship.get_active_chat_all()

    user_id = User.get_current().id
    sponsorships = {}

    for chat_id, chat_title in sponsored_data.items():
        try:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            if not member.is_chat_member():
                chat = await bot.get_chat(chat_id=chat_id)
                chat_url = await chat.get_url()

                sponsorships[chat_url] = chat_title

        except ChatNotFound:
            with suppress(ChatNotFound, BotBlocked):
                await bot.send_message(
                    chat_id=config.bot.CREATOR_ID,
                    text=texts.message.sponsored_error.format(
                        chat_id=chat_id,
                        chat_title=chat_title))

    return sponsorships

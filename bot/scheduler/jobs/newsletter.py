from contextlib import suppress

from aiogram.utils.exceptions import (BotBlocked,
                                      ChatNotFound,
                                      MessageToDeleteNotFound,
                                      MessageCantBeDeleted)

from bot.loader import bot

from bot.texts import texts
from bot.keyboards import keyboards


async def run_newsletter(newsletter_data: dict, chat_id_list: list, creator_id: int):
    text = texts.message.newsletter_started
    markup = await keyboards.inline.delete()

    await bot.send_message(
        chat_id=creator_id,
        text=text,
        reply_markup=markup)

    sent, error = 0, 0

    for user_id in chat_id_list:
        try:
            buttons = dict() if 'newsletter_buttons' not in newsletter_data else newsletter_data['newsletter_buttons']
            markup = await keyboards.inline.newsletter_buttons(buttons=buttons)

            if newsletter_data['newsletter_type'] == 'text':
                text = newsletter_data['newsletter_text']

                await bot.send_message(
                    chat_id=user_id,
                    text=text,
                    reply_markup=markup)
            elif newsletter_data['newsletter_type'] == 'photo':
                photo = newsletter_data['newsletter_photo']
                caption = newsletter_data['newsletter_caption']

                await bot.send_photo(
                    chat_id=user_id,
                    photo=photo,
                    caption=caption,
                    reply_markup=markup)

            sent += 1
        except (ChatNotFound, BotBlocked):
            error += 1

    text = texts.message.newsletter_finished.format(
        sent=sent,
        error=error)
    markup = await keyboards.inline.delete()

    await bot.send_message(
        chat_id=creator_id,
        text=text,
        reply_markup=markup)

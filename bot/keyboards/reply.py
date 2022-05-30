from dataclasses import dataclass

from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)

from bot.texts import texts


@dataclass
class ReplyKeyboard:

    @classmethod
    async def newsletter_create(cls, user_data: dict):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        if 'newsletter_type' in user_data:
            if 'newsletter_buttons' in user_data:
                markup.row(
                    KeyboardButton(text=texts.button.del_buttons))

            else:
                markup.row(
                    KeyboardButton(text=texts.button.add_buttons))

            markup.row(
                KeyboardButton(text=texts.button.back_t),
                KeyboardButton(text=texts.button.next_t))

        else:
            markup.row(
                KeyboardButton(text=texts.button.back_t))

        return markup

    @staticmethod
    async def confirm_back():
        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row(
            KeyboardButton(text=texts.button.back_t),
            KeyboardButton(text=texts.button.confirm))

        return markup

    @staticmethod
    async def back():
        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row(
            KeyboardButton(text=texts.button.back_t))

        return markup

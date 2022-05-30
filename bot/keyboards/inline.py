from dataclasses import dataclass

from aiogram.utils.parts import paginate

from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

from bot.config import config
from bot.database import db
from bot.texts import texts
from bot.keyboards.callback_data import cdata


@dataclass
class InlineKeyboard:

    @classmethod
    async def sponsored(cls, sponsored_data: dict):
        markup = InlineKeyboardMarkup(row_width=1)

        for url, text in sponsored_data.items():
            markup.row(
                InlineKeyboardButton(text=text, url=url))

        markup.row(
            InlineKeyboardButton(text=await db.button.get_text(code='check'), callback_data=cdata.check))

        return markup

    @staticmethod
    async def paginator(text_list: list,
                        callback_data_list: list,
                        curr_page: int,
                        min_page: int,
                        max_page: int,
                        limit: int,
                        search: bool = False,
                        ):
        markup = InlineKeyboardMarkup(row_width=1)

        markup.add(
            *[InlineKeyboardButton(
                text=str(t),
                callback_data=str(d)) for t, d in zip(
                paginate(data=text_list, page=curr_page, limit=limit),
                paginate(data=callback_data_list, page=curr_page, limit=limit))])

        if len(text_list) > limit:
            curr_page = curr_page + 1
            first_page = min_page + 1 if curr_page > min_page + 2 else str()
            last_page = max_page + 1 if curr_page < max_page else str()
            prev_page = curr_page - 1 if curr_page > min_page + 1 else str()
            next_page = curr_page + 1 if curr_page < max_page + 1 else str()

            markup.row(
                InlineKeyboardButton(text=texts.button.first_page.format(first_page=first_page),
                                     callback_data=cdata.first_page),
                InlineKeyboardButton(text=texts.button.prev_page.format(prev_page=prev_page),
                                     callback_data=cdata.prev_page),
                InlineKeyboardButton(text=texts.button.curr_page.format(curr_page=curr_page),
                                     callback_data=cdata.curr_page),
                InlineKeyboardButton(text=texts.button.next_page.format(next_page=next_page),
                                     callback_data=cdata.next_page),
                InlineKeyboardButton(text=texts.button.last_page.format(last_page=last_page),
                                     callback_data=cdata.last_page))
        if search:
            markup.row(
                InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back),
                InlineKeyboardButton(text=texts.button.search, callback_data=cdata.search))
        else:
            markup.row(
                InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def newsletter(cls):
        markup = InlineKeyboardMarkup(row_width=2)

        markup.row(
            InlineKeyboardButton(text=texts.button.postponed, callback_data=cdata.postponed),
            InlineKeyboardButton(text=texts.button.create, callback_data=cdata.create))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def newsletter_choose(cls, buttons: dict):
        markup = InlineKeyboardMarkup(row_width=1)

        for text, url in buttons.items():
            markup.row(
                InlineKeyboardButton(text=text, url=url))

        markup.row(
            InlineKeyboardButton(text=texts.button.edit_time, callback_data=cdata.edit_time),
            InlineKeyboardButton(text=texts.button.del_post, callback_data=cdata.del_post))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def newsletter_buttons(cls, buttons: dict):
        markup = InlineKeyboardMarkup(row_width=1)

        for text, url in buttons.items():
            markup.row(
                InlineKeyboardButton(text=text, url=url))

        return markup

    @classmethod
    async def newsletter_run_or_postpone(cls):
        markup = InlineKeyboardMarkup(row_width=2)

        markup.row(
            InlineKeyboardButton(text=texts.button.postpone, callback_data=cdata.postpone),
            InlineKeyboardButton(text=texts.button.run, callback_data=cdata.run))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def admins_choose(cls, status: str):
        markup = InlineKeyboardMarkup(row_width=1)

        markup.row(
            InlineKeyboardButton(text=texts.button.edit_id, callback_data=cdata.edit_id),
            InlineKeyboardButton(text=texts.button.edit_name, callback_data=cdata.edit_name))

        text = texts.button.switch_to_admin if status == cdata.moder else texts.button.switch_to_moder
        callback_data = cdata.switch_to_admin if status == cdata.moder else cdata.switch_to_moder

        markup.row(
            InlineKeyboardButton(text=text, callback_data=callback_data))
        markup.row(
            InlineKeyboardButton(text=texts.button.switch_to_user, callback_data=cdata.switch_to_user))
        markup.row(InlineKeyboardButton(
            text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def admins_status(cls):
        markup = InlineKeyboardMarkup(row_width=1)

        markup.row(
            InlineKeyboardButton(text=texts.button.admin, callback_data=cdata.admin))
        markup.row(
            InlineKeyboardButton(text=texts.button.moder, callback_data=cdata.moder))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @staticmethod
    async def list_add():
        markup = InlineKeyboardMarkup(row_width=2)

        markup.row(
            InlineKeyboardButton(text=texts.button.list, callback_data=cdata.list),
            InlineKeyboardButton(text=texts.button.add, callback_data=cdata.add))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @staticmethod
    async def sponsorship_choice(status: str):
        markup = InlineKeyboardMarkup(row_width=1)

        text = texts.button.sponsorship_active if status == cdata.sponsorship_inactive \
            else texts.button.sponsorship_inactive
        callback_data = cdata.sponsorship_active if status == cdata.sponsorship_inactive \
            else cdata.sponsorship_inactive

        markup.row(
            InlineKeyboardButton(text=text, callback_data=callback_data))
        markup.row(
            InlineKeyboardButton(text=texts.button.sponsorship_edit_chat_id,
                                 callback_data=cdata.sponsorship_edit_chat_id),
            InlineKeyboardButton(text=texts.button.sponsorship_edit_chat_title,
                                 callback_data=cdata.sponsorship_edit_chat_title))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back),
            InlineKeyboardButton(text=texts.button.delete, callback_data=cdata.delete))

        return markup

    @classmethod
    async def back_confirm(cls):
        markup = InlineKeyboardMarkup(row_width=1)

        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back),
            InlineKeyboardButton(text=texts.button.confirm, callback_data=cdata.confirm))

        return markup

    @classmethod
    async def users_choose(cls, user_state):
        markup = InlineKeyboardMarkup(row_width=1)

        text = texts.button.block if user_state != 'blocked' else texts.button.unblock
        callback_data = cdata.block if user_state != 'blocked' else cdata.unblock

        markup.row(
            InlineKeyboardButton(text=texts.button.send_message, callback_data=cdata.send_message))
        markup.row(
            InlineKeyboardButton(text=text, callback_data=callback_data))
        markup.row(
            InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

    @classmethod
    async def delete(cls):
        markup = InlineKeyboardMarkup(row_width=1)

        markup.row(
            InlineKeyboardButton(text=texts.button.hide, callback_data=cdata.hide))

        return markup

    @classmethod
    async def main_admin(cls, user_id: int):
        markup = InlineKeyboardMarkup(row_width=2)

        admin = await db.admin.get(user_id=user_id)

        if user_id == int(config.bot.CREATOR_ID):
            markup.row(
                InlineKeyboardButton(text=texts.button.admins, callback_data=cdata.admins),
                InlineKeyboardButton(text=texts.button.users, callback_data=cdata.users))
            markup.row(
                InlineKeyboardButton(text=texts.button.messages, callback_data=cdata.messages),
                InlineKeyboardButton(text=texts.button.buttons, callback_data=cdata.buttons))
            markup.row(
                InlineKeyboardButton(text=texts.button.sponsorship, callback_data=cdata.sponsorship),
                InlineKeyboardButton(text=texts.button.newsletter, callback_data=cdata.newsletter))
            markup.row(
                InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back),
                InlineKeyboardButton(text=texts.button.stop, callback_data=cdata.stop),
                InlineKeyboardButton(text=texts.button.reload, callback_data=cdata.reload),)
        else:
            if admin and admin.role == 'admin':
                markup.row(
                    InlineKeyboardButton(text=texts.button.users, callback_data=cdata.users))

            markup.row(
                InlineKeyboardButton(text=texts.button.messages, callback_data=cdata.messages),
                InlineKeyboardButton(text=texts.button.buttons, callback_data=cdata.buttons))

            if admin and admin.role == 'moder':
                markup.row(
                    InlineKeyboardButton(text=texts.button.newsletter, callback_data=cdata.newsletter))

            else:
                markup.row(
                    InlineKeyboardButton(text=texts.button.sponsorship, callback_data=cdata.sponsorship),
                    InlineKeyboardButton(text=texts.button.newsletter, callback_data=cdata.newsletter))

            markup.row(
                InlineKeyboardButton(text=texts.button.back, callback_data=cdata.back))

        return markup

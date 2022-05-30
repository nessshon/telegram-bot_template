from contextlib import suppress

from aiogram.dispatcher import FSMContext

from aiogram.types import (Message,
                           CallbackQuery)

from aiogram.utils.exceptions import (MessageNotModified,
                                      MessageCantBeEdited,
                                      MessageToEditNotFound)

from bot.keyboards import keyboards
from bot.keyboards.callback_data import cdata
from bot.utils.bot.message import delete_message


class Paginator:

    def __init__(self,
                 text_list: list,
                 callback_data_list: list,
                 limit: int = 5
                 ):
        self.limit = limit
        self.text_list = text_list
        self.callback_data_list = callback_data_list
        self.min_page, self.max_page = 0, len(
            [text_list[i:i + limit] for i in range(0, len(text_list), limit)]) - 1 if len(text_list) > limit else 0

    async def send_message(self, message: Message,
                           state: FSMContext,
                           text: str,
                           curr_page: int = 0,
                           search: bool = False
                           ):
        with suppress(MessageNotModified, MessageCantBeEdited, MessageToEditNotFound):
            msg = await message.answer(
                text=text,
                reply_markup=await keyboards.inline.paginator(
                    text_list=self.text_list,
                    callback_data_list=self.callback_data_list,
                    curr_page=curr_page,
                    min_page=self.min_page,
                    max_page=self.max_page,
                    limit=self.limit,
                    search=search))

            await delete_message(message_id2=True)
            await state.update_data(
                curr_page=curr_page,
                message_id=msg.message_id)

    async def edit_text(self, call: CallbackQuery,
                        state: FSMContext,
                        text: str,
                        curr_page: int = 0,
                        search: bool = False
                        ):
        user_data = await state.get_data()
        curr_page = curr_page if 'curr_page' not in user_data else user_data['curr_page']

        with suppress(MessageNotModified, MessageCantBeEdited, MessageToEditNotFound):
            await call.message.edit_text(
                text=text,
                reply_markup=await keyboards.inline.paginator(
                    text_list=self.text_list,
                    callback_data_list=self.callback_data_list,
                    curr_page=curr_page,
                    min_page=self.min_page,
                    max_page=self.max_page,
                    limit=self.limit,
                    search=search))

            await state.update_data(curr_page=curr_page)

    async def edit_reply_markup(self, call: CallbackQuery,
                                state: FSMContext,
                                search: bool = False
                                ):
        user_data = await state.get_data()
        curr_page = user_data.get('curr_page')

        if call.data == cdata.first_page:
            curr_page = self.min_page

        if call.data == cdata.prev_page:
            curr_page = curr_page - 1 if curr_page > self.min_page else self.max_page

        if call.data == cdata.next_page:
            curr_page = curr_page + 1 if curr_page < self.max_page else self.min_page

        if call.data == cdata.last_page:
            curr_page = self.max_page

        with suppress(MessageNotModified, MessageCantBeEdited, MessageToEditNotFound):
            await call.message.edit_reply_markup(
                reply_markup=await keyboards.inline.paginator(
                    text_list=self.text_list,
                    callback_data_list=self.callback_data_list,
                    curr_page=curr_page,
                    min_page=self.min_page,
                    max_page=self.max_page,
                    limit=self.limit,
                    search=search))

        async with state.proxy() as data:
            data.update(curr_page=curr_page)

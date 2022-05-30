from aiogram.types import Message

from aiogram.dispatcher import FSMContext

from bot.database import db
from bot.keyboards import keyboards
from bot.states import states

from bot.utils.bot.message import delete_message
from bot.handlers.users.functions.sponsored import (sponsored,
                                                    get_sponsored)


async def main(message: Message, state: FSMContext):
    sponsored_data = await get_sponsored()

    if any(sponsored_data):
        await delete_message()
        async with state.proxy() as data:
            data.clear()

        await sponsored(
            message=message,
            state=state,
            sponsored_data=sponsored_data)

    else:
        text = await db.message.get_text(code='main')

        msg = await message.answer(
            text=text)
        await delete_message()
        async with state.proxy() as data:
            data.clear()

        await states.user.main.set()
        await state.update_data(message_id=msg.message_id)

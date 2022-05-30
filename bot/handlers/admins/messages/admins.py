from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import BadRequest

from bot.database import db
from bot.handlers.admins.functions.admins import admins, admins_status, admins_add, admins_first_name, admins_choose
from bot.loader import bot
from bot.texts import texts
from bot.utils.bot.message import delete_message, send_auto_delete_message


async def admins_message_handler(message: Message):
    await delete_message(message=message)


async def admins_add_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await admins(message=message, state=state)

        else:
            user_id = message.text if not message.forward_from else message.forward_from.id

            if user_id.isdigit():
                user_id = int(user_id)
                if user_id in await db.user.get_user_id_all():
                    if user_id in await db.admin.get_user_id_all():
                        text = texts.message.admins_add_exists
                        await send_auto_delete_message(message=message, text=text)

                    else:
                        await state.update_data(admin_id=user_id)
                        await admins_first_name(state=state, message=message)
                else:
                    text = texts.message.admins_add_error
                    await send_auto_delete_message(message=message, text=text)

    await delete_message(message=message)


async def admins_first_name_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await admins_add(message=message, state=state)

        else:
            await state.update_data(admin_name=message.text.title())
            await admins_status(message=message, state=state)

    await delete_message(message=message)


async def admins_status_message_handler(message: Message):
    await delete_message(message=message)


async def admins_add_confirm_message_handler(message: Message):
    await delete_message(message=message)


async def admins_choose_message_handler(message: Message):
    await delete_message(message=message)


async def admins_edit_name_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await admins_choose(message=message, state=state)
        else:
            await db.admin.update_first_name(user_id=user_data['admin_id'], first_name=message.text.title())
            await admins_choose(message=message, state=state)

            text = texts.message.admins_name_edited
            await send_auto_delete_message(message=message, text=text)

    await delete_message(message=message)


async def admins_edit_id_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await admins_choose(message=message, state=state)

        else:
            user_id = message.text if not message.forward_from else message.forward_from.id

            if user_id.isdigit():
                user_id = int(user_id)
                if user_id in await db.user.get_user_id_all():
                    if user_id in await db.admin.get_user_id_all():
                        text = texts.message.admins_add_exists
                        await send_auto_delete_message(message=message, text=text)

                    else:
                        await state.update_data(admin_id=user_id)
                        await db.admin.update_id(user_id=user_data['admin_id'], new_user_id=user_id)
                        await admins_choose(state=state, message=message)
                else:
                    text = texts.message.admins_add_error
                    await send_auto_delete_message(message=message, text=text)

    await delete_message(message=message)

import asyncio
import os
from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.config import config
from bot.handlers.admins.functions.admins import admins
from bot.handlers.admins.functions.buttons import buttons_list
from bot.handlers.admins.functions.main import reload_bot, stop_bot, main_admin
from bot.handlers.admins.functions.messages import messages_list
from bot.handlers.admins.functions.newsletter import newsletter
from bot.handlers.admins.functions.sponsorship import sponsorship
from bot.handlers.admins.functions.users import users_list
from bot.handlers.users.functions.main import main
from bot.keyboards.callback_data import cdata
from bot.texts import texts


async def main_admin_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.admins:
        await admins(call=call, state=state)

    elif call.data == cdata.users:
        await users_list(call=call, state=state)

    elif call.data == cdata.messages:
        await messages_list(state=state, call=call)

    elif call.data == cdata.buttons:
        await buttons_list(state=state, call=call)

    elif call.data == cdata.newsletter:
        await newsletter(state=state, call=call)

    elif call.data == cdata.sponsorship:
        await sponsorship(state=state, call=call)

    elif call.data == cdata.back:
        await main(message=call.message, state=state)

    elif call.data == cdata.stop:
        await stop_bot(call=call)

    elif call.data == cdata.reload:
        await reload_bot(call=call)

    await call.answer()


async def reload_bot_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.confirm:
        text, sec = texts.message.reload_bot_info, 5

        await timer_message(call=call, text=text, sec=sec)
        await main(message=call.message, state=state)
        if config.bot.SERVER_PASS:
            os.system(f'echo {config.bot.SERVER_PASS} | sudo -S systemctl restart {config.bot.SERVICE_NAME}')
        else:
            os.system(f'sudo systemctl restart {config.bot.SERVICE_NAME}')


async def stop_bot_callback_handler(call: CallbackQuery, state: FSMContext):
    if call.data == cdata.back:
        await main_admin(call=call, state=state)

    elif call.data == cdata.confirm:
        text, sec = texts.message.stop_bot_info, 5

        await timer_message(call=call, text=text, sec=sec)
        await main(message=call.message, state=state)
        if config.bot.SERVER_PASS:
            os.system(f'echo {config.bot.SERVER_PASS} | sudo -S systemctl restart {config.bot.SERVICE_NAME}')
        else:
            os.system(f'sudo systemctl stop {config.bot.SERVICE_NAME}')


async def timer_message(call: CallbackQuery, text: str, sec: int):
    with suppress(Exception):
        await call.message.edit_text(text=text.format(sec=sec))
        while range(sec):
            sec -= 1
            await asyncio.sleep(1)
            if sec == 0:
                break
            await call.message.edit_text(text=text.format(sec=sec))

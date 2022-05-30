from datetime import datetime

from aiogram.dispatcher import FSMContext

from aiogram.types import Message

from bot.handlers.admins.functions.newsletter import (newsletter_create,
                                                      newsletter,
                                                      newsletter_add_buttons,
                                                      newsletter_run_or_postpone,
                                                      newsletter_choose)
from bot.keyboards.callback_data import cdata
from bot.database import db
from bot.scheduler.jobs.newsletter import run_newsletter
from bot.scheduler.loader import scheduler

from bot.texts import texts

from bot.utils.bot.message import delete_message, send_auto_delete_message


async def newsletter_message_handler(message: Message):
    await delete_message(message=message)


async def newsletter_create_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await newsletter(state=state, message=message)
            async with state.proxy() as data:
                data.pop('newsletter_type')
                data.pop('newsletter_buttons')
            await delete_message(message=message)

        elif message.text == texts.button.add_buttons:
            await newsletter_add_buttons(message=message, state=state)

        elif message.text == texts.button.del_buttons:
            async with state.proxy() as data:
                data.pop('newsletter_buttons')
            await newsletter_create(message=message, state=state)

        elif message.text == texts.button.next_t:
            await newsletter_run_or_postpone(state=state, message=message)

        else:
            await state.update_data(
                newsletter_type='text',
                newsletter_text=message.parse_entities())
            await newsletter_create(message=message, state=state)

    elif message.content_type == 'photo':
        caption = None if not message.caption else message.parse_entities()

        await state.update_data(
            newsletter_type='photo',
            newsletter_photo=message.photo[-1].file_id,
            newsletter_caption=caption)
        await newsletter_create(message=message, state=state)

    await delete_message(message=message)


async def newsletter_add_buttons_message_handler(message: Message, state: FSMContext):
    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await newsletter_create(message=message, state=state)

        elif '|' in message.text[1:-1] and 'entities' in message and 'url' in message['entities'][0]['type']:
            buttons = dict(
                (key.strip(), val.strip()) for key, val in (item.split('|') for item in message.text.split('\n')))
            await state.update_data(newsletter_buttons=buttons)
            await newsletter_create(message=message, state=state)

    await delete_message(message=message)


async def newsletter_run_or_postpone_message_handler(message: Message):
    await delete_message(message=message)


async def newsletter_run_confirm_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await newsletter_run_or_postpone(state=state, message=message)

        elif message.text == texts.button.confirm:
            await newsletter(message=message, state=state)

            newsletter_data = user_data
            creator_id = message.from_user.id
            chat_id_list = await db.user.get_user_id_all()

            await run_newsletter(
                newsletter_data=newsletter_data,
                chat_id_list=chat_id_list,
                creator_id=creator_id)

    await delete_message(message=message)


async def newsletter_postpone_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await newsletter_run_or_postpone(state=state, message=message)

        else:
            try:
                datetime_a = datetime.strptime(message.text, '%H %M %d %m %Y')
                datetime_b = datetime_a.strftime("%H:%M %-d %b %Y г")
                datetime_c = datetime_a.strftime('%Y-%m-%d %H:%M')

                if datetime_a > datetime.now():
                    if datetime_c in [str(i)[:-9] for i in [i.next_run_time for i in scheduler.get_jobs()]]:
                        text = texts.message.newsletter_date_time_exists

                        await send_auto_delete_message(
                            message=message,
                            text=text)

                    else:
                        await newsletter(message=message, state=state)

                        newsletter_data = user_data
                        chat_id_list = await db.user.get_user_id_all()
                        creator_id = message.from_user.id

                        scheduler.add_job(
                            id=datetime_c,
                            func=run_newsletter,
                            trigger='date',
                            run_date=datetime_a,
                            args=(
                                newsletter_data,
                                chat_id_list,
                                creator_id))
                        text = texts.message.newsletter_postponed_done.format(datetime_b=datetime_b)

                        await send_auto_delete_message(
                            message=message,
                            text=text)

                else:
                    text = texts.message.newsletter_date_time_more

                    await send_auto_delete_message(
                        message=message,
                        text=text)

            except ValueError:
                datetime_a = datetime.now().strftime('%H %M %d %m %Y')
                datetime_b = datetime.now().strftime("%H:%M %-d %b %Y г")

                text = texts.message.newsletter_date_time_error.format(
                    datetime_a=datetime_a,
                    datetime_b=datetime_b)
                await send_auto_delete_message(
                    message=message,
                    text=text)

    await delete_message(message=message)


async def newsletter_postponed_message_handler(message: Message):
    await delete_message(message=message)


async def newsletter_choose_message_handler(message: Message):
    await delete_message(message=message)


async def newsletter_edit_time_message_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()

    if message.content_type == 'text':
        if message.text == texts.button.back_t:
            await newsletter_choose(state=state, message=message)
        else:
            try:
                datetime_a = datetime.strptime(message.text, '%H %M %d %m %Y')
                datetime_b = datetime_a.strftime("%H:%M %-d %b %Y г")
                datetime_c = datetime_a.strftime('%Y-%m-%d %H:%M')

                if datetime_a > datetime.now():
                    if datetime_c in [str(i)[:-9] for i in [i.next_run_time for i in scheduler.get_jobs()]]:
                        text = texts.message.newsletter_date_time_exists

                        await send_auto_delete_message(
                            message=message,
                            text=text)

                    else:
                        job = scheduler.get_job(job_id=user_data['job_id'])
                        newsletter_data = job.args[0]
                        chat_id_list = job.args[1]
                        creator_id = job.args[2]

                        scheduler.add_job(
                            id=datetime_c,
                            func=run_newsletter,
                            trigger='date',
                            run_date=datetime_a,
                            args=(
                                newsletter_data,
                                chat_id_list,
                                creator_id))
                        scheduler.remove_job(job_id=user_data['job_id'])

                        await state.update_data(job_id=datetime_c)
                        await newsletter_choose(state=state, message=message)

                        text = texts.message.newsletter_postponed_done.format(datetime_b=datetime_b)
                        await send_auto_delete_message(
                            message=message,
                            text=text)
                else:
                    text = texts.message.newsletter_date_time_more

                    await send_auto_delete_message(
                        message=message,
                        text=text)

            except ValueError:
                datetime_a = datetime.now().strftime('%H %M %d %m %Y')
                datetime_b = datetime.now().strftime("%H:%M %-d %b %Y г")

                text = texts.message.newsletter_date_time_error.format(
                    datetime_a=datetime_a,
                    datetime_b=datetime_b)
                await send_auto_delete_message(
                    message=message,
                    text=text)

    await delete_message(message=message)


async def newsletter_delete_message_handler(message: Message):
    await delete_message(message=message)

from aiogram import Dispatcher

from bot.handlers.admins.callbacks.admins import admins_callback_handler, admins_status_callback_handler, \
    admins_add_confirm_callback_handler, admins_list_callback_handler, admins_choose_callback_handler
from bot.handlers.admins.callbacks.main import main_admin_callback_handler, reload_bot_callback_handler, \
    stop_bot_callback_handler
from bot.handlers.admins.callbacks.messages import messages_list_callback_handler
from bot.handlers.admins.callbacks.buttons import buttons_list_callback_handler
from bot.handlers.admins.callbacks.newsletter import (newsletter_callback_handler,
                                                      newsletter_run_or_postpone_callback_handler,
                                                      newsletter_postponed_callback_handler,
                                                      newsletter_choose_callback_handler,
                                                      newsletter_delete_callback_handler)
from bot.handlers.admins.callbacks.sponsorship import (sponsorship_callback_handler,
                                                       sponsorship_list_callback_handler,
                                                       sponsorship_choice_callback_handler)
from bot.handlers.admins.callbacks.users import users_list_callback_handler, users_choose_callback_handler

from bot.states import states


def register_admin_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        main_admin_callback_handler,
        state=states.admin.main)
    dp.register_callback_query_handler(
        reload_bot_callback_handler,
        state=states.admin.reload_bot)
    dp.register_callback_query_handler(
        stop_bot_callback_handler,
        state=states.admin.stop_bot)
    # -----sponsorship
    dp.register_callback_query_handler(
        sponsorship_callback_handler,
        state=states.admin.sponsorship)
    dp.register_callback_query_handler(
        sponsorship_list_callback_handler,
        state=states.admin.sponsorship_list)
    dp.register_callback_query_handler(
        sponsorship_choice_callback_handler,
        state=states.admin.sponsorship_choice)
    # -----messages
    dp.register_callback_query_handler(
        messages_list_callback_handler,
        state=states.admin.messages_list)
    # -----buttons
    dp.register_callback_query_handler(
        buttons_list_callback_handler,
        state=states.admin.buttons_list)
    # -----newsletter
    dp.register_callback_query_handler(
        newsletter_callback_handler,
        state=states.admin.newsletter)
    dp.register_callback_query_handler(
        newsletter_run_or_postpone_callback_handler,
        state=states.admin.newsletter_run_or_postpone)
    dp.register_callback_query_handler(
        newsletter_postponed_callback_handler,
        state=states.admin.newsletter_postponed)
    dp.register_callback_query_handler(
        newsletter_choose_callback_handler,
        state=states.admin.newsletter_choose)
    dp.register_callback_query_handler(
        newsletter_delete_callback_handler,
        state=states.admin.newsletter_delete)
    # -----admins
    dp.register_callback_query_handler(
        admins_callback_handler,
        state=states.admin.admins)
    dp.register_callback_query_handler(
        admins_status_callback_handler,
        state=states.admin.admins_status)
    dp.register_callback_query_handler(
        admins_add_confirm_callback_handler,
        state=states.admin.admins_add_confirm)
    dp.register_callback_query_handler(
        admins_list_callback_handler,
        state=states.admin.admins_list)
    dp.register_callback_query_handler(
        admins_choose_callback_handler,
        state=states.admin.admins_choose)
    # -----users
    dp.register_callback_query_handler(
        users_list_callback_handler,
        state=states.admin.users_list)
    dp.register_callback_query_handler(
        users_choose_callback_handler,
        state=states.admin.users_choose)

from aiogram import Dispatcher

from bot.handlers.admins.messages.admins import (admins_message_handler,
                                                 admins_add_message_handler,
                                                 admins_status_message_handler,
                                                 admins_add_confirm_message_handler,
                                                 admins_first_name_message_handler,
                                                 admins_choose_message_handler,
                                                 admins_edit_name_message_handler,
                                                 admins_edit_id_message_handler)

from bot.handlers.admins.messages.main import main_admin_message_handler

from bot.handlers.admins.messages.messages import (messages_list_message_handler,
                                                   messages_send_text_message_handler,
                                                   messages_confirm_message_handler,
                                                   messages_search_message_handler)

from bot.handlers.admins.messages.buttons import (buttons_list_message_handler,
                                                  buttons_send_text_message_handler,
                                                  buttons_confirm_message_handler,
                                                  buttons_search_message_handler)

from bot.handlers.admins.messages.newsletter import (newsletter_message_handler,
                                                     newsletter_create_message_handler,
                                                     newsletter_add_buttons_message_handler,
                                                     newsletter_run_or_postpone_message_handler,
                                                     newsletter_run_confirm_message_handler,
                                                     newsletter_postpone_message_handler,
                                                     newsletter_postponed_message_handler,
                                                     newsletter_choose_message_handler,
                                                     newsletter_edit_time_message_handler,
                                                     newsletter_delete_message_handler)

from bot.handlers.admins.messages.sponsorship import (sponsorship_message_handler,
                                                      sponsorship_list_message_handler,
                                                      sponsorship_edit_choice_message_handler,
                                                      sponsorship_edit_chat_id_message_handler,
                                                      sponsorship_edit_chat_title_message_handler,
                                                      sponsorship_delete_message_handler,
                                                      sponsorship_send_chat_id_message_handler,
                                                      sponsorship_send_chat_title_message_handler,
                                                      sponsorship_add_message_handler)

from bot.handlers.admins.messages.users import (users_list_message_handler,
                                                users_choose_message_handler,
                                                users_search_message_handler,
                                                users_send_message_message_handler,
                                                users_send_message_confirm_message_handler)

from bot.states import states


def register_admin_message_handlers(dp: Dispatcher):
    dp.register_message_handler(
        main_admin_message_handler,
        state=states.admin.main,
        content_types='any')
    # -----sponsorship
    dp.register_message_handler(
        sponsorship_message_handler,
        state=states.admin.sponsorship,
        content_types='any')
    dp.register_message_handler(
        sponsorship_list_message_handler,
        state=states.admin.sponsorship_list,
        content_types='any')
    dp.register_message_handler(
        sponsorship_edit_choice_message_handler,
        state=states.admin.sponsorship_choice,
        content_types='any')
    dp.register_message_handler(
        sponsorship_edit_chat_id_message_handler,
        state=states.admin.sponsorship_edit_chat_id,
        content_types='any')
    dp.register_message_handler(
        sponsorship_edit_chat_title_message_handler,
        state=states.admin.sponsorship_edit_chat_title,
        content_types='any')
    dp.register_message_handler(
        sponsorship_delete_message_handler,
        state=states.admin.sponsorship_delete,
        content_types='any')
    dp.register_message_handler(
        sponsorship_send_chat_id_message_handler,
        state=states.admin.sponsorship_send_chat_id,
        content_types='any')
    dp.register_message_handler(
        sponsorship_send_chat_title_message_handler,
        state=states.admin.sponsorship_send_chat_title,
        content_types='any')
    dp.register_message_handler(
        sponsorship_add_message_handler,
        state=states.admin.sponsorship_add,
        content_types='any')
    # -----messages
    dp.register_message_handler(
        messages_list_message_handler,
        state=states.admin.messages_list,
        content_types='any')
    dp.register_message_handler(
        messages_send_text_message_handler,
        state=states.admin.messages_send_text,
        content_types='any')
    dp.register_message_handler(
        messages_confirm_message_handler,
        state=states.admin.messages_confirm,
        content_types='any')
    dp.register_message_handler(
        messages_search_message_handler,
        state=states.admin.messages_search,
        content_types='any')
    # -----buttons
    dp.register_message_handler(
        buttons_list_message_handler,
        state=states.admin.buttons_list,
        content_types='any')
    dp.register_message_handler(
        buttons_send_text_message_handler,
        state=states.admin.buttons_send_text,
        content_types='any')
    dp.register_message_handler(
        buttons_confirm_message_handler,
        state=states.admin.buttons_confirm,
        content_types='any')
    dp.register_message_handler(
        buttons_search_message_handler,
        state=states.admin.buttons_search,
        content_types='any')
    # -----newsletter
    dp.register_message_handler(
        newsletter_message_handler,
        state=states.admin.newsletter,
        content_types='any')
    dp.register_message_handler(
        newsletter_create_message_handler,
        state=states.admin.newsletter_create,
        content_types='any')
    dp.register_message_handler(
        newsletter_add_buttons_message_handler,
        state=states.admin.newsletter_add_buttons,
        content_types='any')
    dp.register_message_handler(
        newsletter_run_or_postpone_message_handler,
        state=states.admin.newsletter_run_or_postpone,
        content_types='any')
    dp.register_message_handler(
        newsletter_run_confirm_message_handler,
        state=states.admin.newsletter_run_confirm,
        content_types='any')
    dp.register_message_handler(
        newsletter_postpone_message_handler,
        state=states.admin.newsletter_postpone,
        content_types='any')
    dp.register_message_handler(
        newsletter_postponed_message_handler,
        state=states.admin.newsletter_postponed,
        content_types='any')
    dp.register_message_handler(
        newsletter_choose_message_handler,
        state=states.admin.newsletter_choose,
        content_types='any')
    dp.register_message_handler(
        newsletter_edit_time_message_handler,
        state=states.admin.newsletter_edit_time,
        content_types='any')
    dp.register_message_handler(
        newsletter_delete_message_handler,
        state=states.admin.newsletter_delete,
        content_types='any')
    # -----admins
    dp.register_message_handler(
        admins_message_handler,
        state=states.admin.admins,
        content_types='any')
    dp.register_message_handler(
        admins_add_message_handler,
        state=states.admin.admins_add,
        content_types='any')
    dp.register_message_handler(
        admins_first_name_message_handler,
        state=states.admin.admins_first_name,
        content_types='any')
    dp.register_message_handler(
        admins_status_message_handler,
        state=states.admin.admins_status,
        content_types='any')
    dp.register_message_handler(
        admins_add_confirm_message_handler,
        state=states.admin.admins_add_confirm,
        content_types='any')
    dp.register_message_handler(
        admins_choose_message_handler,
        state=states.admin.admins_choose,
        content_types='any')
    dp.register_message_handler(
        admins_edit_name_message_handler,
        state=states.admin.admins_edit_name,
        content_types='any')
    dp.register_message_handler(
        admins_edit_id_message_handler,
        state=states.admin.admins_edit_id,
        content_types='any')
    # -----users
    dp.register_message_handler(
        users_list_message_handler,
        state=states.admin.users_list,
        content_types='any')
    dp.register_message_handler(
        users_choose_message_handler,
        state=states.admin.users_choose,
        content_types='any')
    dp.register_message_handler(
        users_search_message_handler,
        state=states.admin.users_search,
        content_types='any')
    dp.register_message_handler(
        users_send_message_message_handler,
        state=states.admin.users_send_message,
        content_types='any')
    dp.register_message_handler(
        users_send_message_confirm_message_handler,
        state=states.admin.users_send_message_confirm,
        content_types='any')

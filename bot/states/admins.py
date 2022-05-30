from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    main = State()
    stop_bot = State()
    reload_bot = State()
    # -----sponsorship
    sponsorship = State()
    sponsorship_list = State()
    sponsorship_choice = State()
    sponsorship_edit_chat_id = State()
    sponsorship_edit_chat_title = State()
    sponsorship_delete = State()
    sponsorship_send_chat_id = State()
    sponsorship_send_chat_title = State()
    sponsorship_add = State()
    # -----messages
    messages_list = State()
    messages_choice = State()
    messages_send_text = State()
    messages_confirm = State()
    messages_search = State()
    # -----buttons
    buttons_list = State()
    buttons_choice = State()
    buttons_send_text = State()
    buttons_confirm = State()
    buttons_search = State()
    # -----newsletter
    newsletter = State()
    newsletter_create = State()
    newsletter_add_buttons = State()
    newsletter_run_or_postpone = State()
    newsletter_run_confirm = State()
    newsletter_postpone = State()
    newsletter_postpone_confirm = State()
    newsletter_postponed = State()
    newsletter_choose = State()
    newsletter_edit_time = State()
    newsletter_delete = State()
    # -----admins
    admins = State()
    admins_list = State()
    admins_choose = State()
    admins_add = State()
    admins_first_name = State()
    admins_status = State()
    admins_add_confirm = State()
    admins_edit_name = State()
    admins_edit_id = State()
    # -----users
    users_list = State()
    users_choose = State()
    users_search = State()
    users_send_message = State()
    users_send_message_confirm = State()
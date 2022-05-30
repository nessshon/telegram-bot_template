from dataclasses import dataclass


@dataclass
class CallbackData:
    ru = 'ru'
    en = 'en'
    add = 'add'
    delete = 'delete'
    hide = 'hide'
    list = 'list'
    confirm = 'confirm'
    back = 'back'
    next = 'next'
    check = 'check'
    reload = 'reload'
    stop = 'stop'
    search = 'search'
    clean = 'clean'
    first_page = 'first_page'
    prev_page = 'prev_page'
    curr_page = 'curr_page'
    next_page = 'next_page'
    last_page = 'last_page'
    admins = 'admins'
    users = 'users'
    messages = 'messages'
    buttons = 'buttons'
    newsletter = 'newsletter'
    sponsorship = 'sponsorship'
    # -----sponsorship
    sponsorship_active = 'active'
    sponsorship_inactive = 'inactive'
    sponsorship_edit_chat_id = 'Изменить ID'
    sponsorship_edit_chat_title = 'Изменить название'
    # -----newsletter
    create = 'create'
    postponed = 'postponed'
    add_buttons = 'add_buttons'
    del_buttons = 'del_buttons'
    run = 'run'
    postpone = 'postpone'
    send_all = 'send_all'
    del_post = 'del_post'
    edit_time = 'edit_time'
    # -----admins
    admin = 'admin'
    moder = 'moder'
    switch_to_moder = 'switch_to_moder'
    switch_to_admin = 'switch_to_admin'
    switch_to_user = 'switch_to_user'
    edit_name = 'edit_name'
    edit_id = 'edit_id'
    # -----users
    block = 'block'
    unblock = 'unblock'
    send_message = 'send_message'
    reply_message = 'reply_message'


cdata = CallbackData()

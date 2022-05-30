from dataclasses import dataclass


@dataclass
class MessageText:
    bot_started = '<b>Бот запущен!</b>\n\n/start - Перезапустить бота.'
    bot_stopped = '<b>Бот остановлен!</b>'
    user_started_bot = '#Пользователь {user} <b>запустил(а)</b> бота!'
    user_stopped_bot = '#Пользователь {user} <b>остановил(а)</b> бота!'
    user_restarted_bot = '#Пользователь {user} <b>перезапустил(а)</b> бота!'
    error_info = (
        '#ERROR {datetime}\n\n'
        '<b>User:</b> {user}\n\n'
        '<b>Update:</b>\n'
        '{update}\n\n'
        '<b>Exception:</b>\n'
        '{exception}\n\n')
    error_traceback = (
        '<b>Traceback:</b>\n'
        '{traceback}')
    sponsored_error = (
        'Чат <b>{chat_title}</b>[ID: <code>{chat_id}</code>] не найден!')

    main_admin = (
        '<b>Панель администратора</b>')
    stop_bot = (
        '<b>Внимание! Бот будет остановлен!</b>\n\n'
        'Подтвердить остановку бота?')
    stop_bot_info = (
        '<b>Бот будет остановлен через {sec}</b>!')
    reload_bot = (
        '<b>Внимание! Бот будет перезагружен!</b>\n\n'
        'Подтвердить перезагрузку бота?')
    reload_bot_info = (
        '<b>Бот будет перезагружен через {sec}</b>!')
    # -----sponsorship
    sponsorship = (
        '<b>Спонсируемые чаты</b>\n\n'
        '<b>Список</b> - просмотр и редактирование\n'
        '<b>Добавить</b> - добавить спонсорский чат')
    sponsorship_list = (
        '<b>Выберите чат для редактирования:</b>')
    sponsorship_info = (
        'Нет спонсируемых чатов')
    sponsorship_choice = (
        '<b>Название чата:</b>\n'
        '{chat_title}\n\n'
        '<b>Чат ID:</b>\n'
        '<code>{chat_id}</code>\n\n'
        '<b>Статус:</b>\n'
        '{status}\n\n'
        '<b>Ссылка на чат:</b>\n'
        '{chat_url}')
    sponsorship_edit_chat_id = (
        '<b>Старый чат ID:</b>\n'
        '<code>{chat_id}</code>\n\n'
        'Отправьте новый чат ID:')
    sponsorship_edited_chat_id = (
        '<b>Чат ID изменен!</b>')
    sponsorship_edit_chat_title = (
        '<b>Старое название чата:</b>\n'
        '{chat_title}\n\n'
        'Отправьте новое название чата:')
    sponsorship_edited_chat_title = (
        '<b>Название чата изменено!</b>')
    sponsorship_send_chat_id = (
        '<b>Отправьте чат ID:</b>\n\n'
        'Бот должен иметь права администратора.')
    sponsorship_chat_not_found = (
        '<b>Чат не найден!</b>\n\n'
        'Бот должен иметь права администратора.')
    sponsorship_chat_exists = (
        '<b>Этот чат ID уже есть в базе.</b>\n\n'
        'Отправьте другой чат ID:')
    sponsorship_send_chat_title = (
        '<b>Отправьте название чата:</b>')
    sponsorship_add = (
        '<b>Название чата:</b>\n'
        '{chat_title}\n\n'
        '<b>Чат ID:</b>\n'
        '<code>{chat_id}</code>\n\n'
        '<b>Ссылка на чат:</b>\n'
        '{chat_url}\n\n'
        '<b>Подтвердить добавление чата?</b>')
    sponsorship_added = (
        '<b>Сонсорский чат добавлен!</b>')
    sponsorship_delete = (
        '<b>Название чата:</b>\n'
        '{chat_title}\n\n'
        '<b>Чат ID:</b>\n'
        '<code>{chat_id}</code>\n\n'
        '<b>Ссылка на чат:</b>\n'
        '{chat_url}\n\n'
        '<b>Подтвердить удаление чата?</b>')
    sponsorship_deleted = (
        '<b>Спонсорский чат удален!</b>')
    # -----messages
    messages_list = (
        '<b>Редактор сообщений</b>\n\n'
        'Выберите сообщение для редактирвоания:')
    messages_send_text = (
        '<b>Исходный текст сообщения:</b>\n'
        '{text_original}\n\n'
        '<b>Отправьте новый текст сообщения:</b>')
    messages_confirm = (
        '<b>Старый текст сообщения:</b>\n'
        '{text_original}\n\n'
        '<b>Новый текст сообщения:</b>\n'
        '{text_new}\n\n'
        '<b>Подтвердить редактирование?</b>')
    messages_search = (
        '<b>Отправьте слово, или отрывок сообщения:</b>')
    messages_find = (
        '<b>Найдено совпадений: {count}</b>\n\n'
        '<b>Выберите сообщение для редактирования:</b>')
    messages_not_find = (
        '<b>Сообщение не найдено!</b>')
    messages_edited = (
        '<b>Сообщение отредактировано!</b>')
    # -----buttons
    buttons_list = (
        '<b>Редактор кнопок</b>\n\n'
        'Выберите кнопку для редактирвоания:')
    buttons_send_text = (
        '<b>Исходный текст кнопки:</b>\n'
        '{text_original}\n\n'
        '<b>Отправьте новый текст кнопки:</b>')
    buttons_confirm = (
        '<b>Старый текст кнопки:</b>\n'
        '{text_original}\n\n'
        '<b>Новый текст кнопки:</b>\n'
        '{text_new}\n\n'
        '<b>Подтвердить редактирование?</b>')
    buttons_search = (
        '<b>Отправьте текст кнопки, или отрывок текста:</b>')
    buttons_find = (
        '<b>Найдено совпадений: {count}</b>\n\n'
        'Выберите кнопку для редактирования:')
    buttons_not_find = (
        '<b>Кнопка не найдена!</b>')
    buttons_edited = (
        '<b>Кнопка отредактирована!</b>')
    # -----newsletter
    newsletter = (
        '<b>Рассылка сообщений</b>\n\n'
        '<b>Создать</b> - создать новое сообщение\n'
        '<b>Отложенные</b> - редактировать сообщение')
    newsletter_create = (
        '<b>Отправьте или перешлите сообщение:</b>')
    newsletter_create_error = (
        '<b>Сперва отправьте сообщение для рассылки.</b>')
    newsletter_add_buttons = (
        '<b>Отправьте список URL-кнопок в одном сообщении, следуя формату ниже:</b>\n\n'
        '<code>Кнопка 1 | http://example1.com\n'
        'Кнопка 2 | http://example2.com\n'
        'Кнопка 3 | http://example3.com</code>\n'
        '...')
    newsletter_added_buttons = (
        '<b>URL-кнопки сохранены!</b>')
    newsletter_deleted_buttons = (
        '<b>URL-кнопки удалены!</b>')
    newsletter_buttons_error = (
        '<b>Вы отправили что-то не внятное.</b>\n'
        'Отправьте кнопки следуя формату ниже:\n\n'
        '<code>Кнопка 1 | http://example1.com\n'
        'Кнопка 2 | http://example2.com\n'
        'Кнопка 3 | http://example3.com</code>\n'
        '...')
    newsletter_run_or_postpone = (
        '<b>Запустить или отложить рассылку сообщений?</b>')
    newsletter_run_confirm = (
        '<b>Проверьте исходное сообщение выше!</b>\n\n'
        'Подтвердить рассылку сообщений?')
    newsletter_date_time = (
        '<b>Отправьте дату и время, следуя формату ниже:</b>\n\n'
        '<code>{datetime_a}</code>  ⇾  {datetime_b}')
    newsletter_date_time_error = (
        '<b>Вы отправили неверную дату и время.</b>\n'
        'Отправьте дату и время следуя формату ниже:\n\n'
        '<code>{datetime_a}</code>  ⇾  {datetime_b}')
    newsletter_date_time_more = (
        '<b>Время должно быть больше текущего на 1 минуту.</b>')
    newsletter_date_time_exists = (
        '<b>Рассылка на дату {datetime_b},\n'
        'уже существует.</b>\n\n'
        'Отправьте другую дату и время:')
    newsletter_postponed_done = (
        '<b>Рассылка отложена</b> до <code>{datetime_b}.</code>')
    newsletter_postpone_confirm = (
        '<b>Подтвердить добавление отоложенного сообщения?</b>')
    newsletter_postponed = (
        '<b>Выберите отложенный пост:</b>')
    newsletter_postponed_info = (
        'Нет отложенных постов')
    newsletter_edit_time = (
        '<b>Подтвердить изменение даты и времени?</b>')
    newsletter_delete = (
        '<b>Подтвердить удаление отложенного сообщения?</b>')
    newsletter_deleted = (
        '<b>Отложенный пост удален!</b>')
    newsletter_started = (
        '<b>Рассылка запущена!</b>')
    newsletter_finished = (
        '<b>Рассылка завершена!</b>\n\n'
        'Доставленно - <b>{sent}</b>\n'
        'Не доставлено - <b>{error}</b>')
    # -----admins
    admins = (
        '<b>Управление администраторами</b>\n\n'
        '<b>Список</b> - управление администраторами\n'
        '<b>Добавить</b> - добавить администратора')
    admins_add = (
        '<b>Отправьте ID или перешлите сообщение от администратора:</b>')
    admins_add_error = (
        '<b>Пользователь не найден!</b>')
    admins_add_exists = (
        '<b>Пользователь с этим ID уже является администратором!</b>')
    admins_first_name = (
        '<b>Отправьте имя администратора:</b>')
    admins_status = (
        '<b>Выберите статус администратора:</b>\n\n')
    admins_add_confirm = (
        '{url}\n\n'
        '<b>ID:</b>\n'
        '{user_id}\n\n'
        '<b>Статус:</b>\n'
        '{status}\n\n'
        '<b>Подтвердить добавление администратора?</b>')
    admins_added = (
        '<b>Администратор {url} добавлен!</b>')
    admins_list = (
        '<b>Выберите администратора:</b>')
    admins_list_info = (
        'Нет администраторов')
    admins_choose = (
        '{url}\n\n'
        '<b>ID:</b>\n'
        '{user_id}\n\n'
        '<b>Статус:</b>\n'
        '{status}\n\n')
    admins_edit_name = (
        '<b>Отправьте новое имя администратора:</b>')
    admins_name_edited = (
        '<b>Имя администратора изменено!</b>')
    admins_edit_id = (
        '<b>Отправьте новый ID или перешлите сообщение от администратора:</b>')
    admins_id_edited = (
        '<b>ID администратора изменен!</b>')
    # -----users
    users_list = (
        '<b>Управление пользователями</b>\n\n'
        'Выберите пользователя:')
    users_choose = (
        '{url}\n\n'
        '<b>Состояние:</b>\n'
        '{state}\n\n'
        '<b>ID пользователя:</b>\n'
        '<code>{user_id}</code>\n\n'
        '<b>Дата регистрации:</b>\n'
        '<code>{created_at}</code>')
    users_search = (
        '<b>Отправьте ID или имя пользователя:</b>')
    users_search_info = (
        '<b>Пользователь не найден!<b>')
    users_find = (
        '<b>Найдено совпадений: {count}</b>\n\n'
        'Выберите пользователя:')
    users_not_blocked = (
        'Нельзя заблокировать создателя!')
    users_not_blocked2 = (
        'Нельзя заблокировать самого себя!')
    users_not_find = (
        '<b>Пользователь не найдена!</b>')
    users_send_message = (
        '<b>Отправьте сообщение:</b>')
    users_send_message_confirm = (
        '<b>Проверьте исходное сообщение выше!</b>\n\n'
        'Подтвердить отправку сообщения?')
    users_message_sent = (
        '<b>Сообщение отправлено пользователю {url}!</b>')
    users_send_message_err = (
        '<b>Сообщение не отправлено!</b>\n\nПользователь остановил или удалил бота.')

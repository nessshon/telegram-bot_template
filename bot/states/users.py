from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    sponsored = State()
    main = State()

    send_message = State()

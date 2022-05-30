from bot.database import MessageModel

data_messages = [
    MessageModel(
        code='throttling',
        desc='Сообщение: защита от спама',
        ru='Подождите {limit} сек!',
    ),
    MessageModel(
        code='blocked',
        desc='Сообщение: блокирован',
        ru='Вы заблокированы!',
    ),
    MessageModel(
        code='sponsored',
        desc='Сообщение: спонсорское',
        ru='Для продолжения подпишитесь на канал(ы):',
    ),
    MessageModel(
        code='sponsored_info',
        desc='Информация: спонсорское',
        ru='Сперва подпишитесь на канал(ы)',
    ),
    MessageModel(
        code='main',
        desc='Сообщение: главное меню',
        ru=(
            'Главное меню'
        ),
    ),
]
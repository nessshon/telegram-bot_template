from dataclasses import dataclass

from bot.keyboards.callback_data import CallbackData
from bot.keyboards.inline import InlineKeyboard
from bot.keyboards.reply import ReplyKeyboard


@dataclass
class Keyboards:
    inline: InlineKeyboard
    reply: ReplyKeyboard


keyboards = Keyboards(
    inline=InlineKeyboard(),
    reply=ReplyKeyboard(),
)

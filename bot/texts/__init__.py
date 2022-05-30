from dataclasses import dataclass

from bot.texts.buttons import ButtonText
from bot.texts.messages import MessageText


@dataclass
class Texts:
    button: ButtonText
    message: MessageText


texts = Texts(
    button=ButtonText(),
    message=MessageText(),
)

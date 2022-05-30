from dataclasses import dataclass

from bot.states.admins import AdminState
from bot.states.users import UserState


@dataclass
class States:
    admin: AdminState
    user: UserState


states = States(
    admin=AdminState(),
    user=UserState(),
)

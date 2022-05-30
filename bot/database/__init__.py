from dataclasses import dataclass

from .models.users import UserModel
from .models.admins import AdminModel
from .models.buttons import ButtonModel
from .models.messages import MessageModel
from .models.sponsorship import SponsorshipModel


@dataclass
class Database:
    user: UserModel
    admin: AdminModel
    button: ButtonModel
    message: MessageModel
    sponsorship: SponsorshipModel


db = Database(
    user=UserModel(),
    admin=AdminModel(),
    button=ButtonModel(),
    message=MessageModel(),
    sponsorship=SponsorshipModel(),
)

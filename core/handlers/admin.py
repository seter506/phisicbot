from aiogram.types import Message
from core.settings import settings

def get_adm_menu(message: Message):
    if message.from_user.id==
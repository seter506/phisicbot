from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from aiogram.types import ContentType
from core.keyboards.reg_kb import reg_kb
import emoji
from utils.db_class import DataBase

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id,text='Бот запущен.')

async def stop_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id,text='Бот остановлен.')

async def get_start(message: Message):
    db=DataBase('utils/database.db')
    if db.client_exists(message.from_user.id):
        if db.client_confirm(message.from_user.id):
            await message.answer(f'Вы зарегистрированы и подтверждены.')
        else:
            await message.answer(f'Вы зарегистрированы, подождите подтверждение вашей заявки.')
    else:
        await message.answer(emoji.emojize('Привет! Этот бот служит для получения и выполнения дополнительных заданий '
                                           f'по физике. Прежде чем использовать бота необходимо зарегистрироваться.'
                                           f' :backhand_index_pointing_down:'),
                             reply_markup=reg_kb)

async def get_image(message: Message, bot: Bot):
    await message.answer(f'Сохраняю картинку...')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


def register_basic_handlers(dp:Dispatcher):
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_image,F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
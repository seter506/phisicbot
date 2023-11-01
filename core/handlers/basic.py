from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from aiogram.types import ContentType
from core.keyboards.reg_kb import reg_kb

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id,text='Бот запущен.')

async def stop_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id,text='Бот остановлен.')

async def get_start(message: Message):
    await message.answer(f'Привет! Этот бот служит для получения и выполнения дополнительных заданий '
                         f'по физике. Прежде чем использовать бота необходимо зарегистрироваться.',
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
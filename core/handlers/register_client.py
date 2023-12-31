from aiogram import Dispatcher,F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import StepsReg
from aiogram.filters import Command
from core.keyboards.reg_kb import klass_kb, conf_kb
from aiogram.types import ContentType
from utils.db_class import DataBase
from core.settings import settings


async def reg_start(message:Message,state:FSMContext):
    await message.answer(f'Начинаем регистрацию. Введите свое имя.')
    await state.set_state(StepsReg.GET_NAME)

async def get_name(message: Message, state:FSMContext):
    await message.answer(f'Теперь введите свою фамилию:')
    await state.update_data(name=message.text)
    await state.set_state(StepsReg.GET_LAST_NAME)

async def get_klass(message: Message, state: FSMContext):
    await message.answer(f'Выберите свой класс:',reply_markup=klass_kb())
    await state.update_data(last_name=message.text)
    await state.set_state(StepsReg.GET_KLASS)

async def reg_confirm(message: Message, state: FSMContext):
    await state.update_data(klass=message.text)
    client_data=await state.get_data()
    name=client_data.get('name')
    last_name=client_data.get('last_name')
    klass=client_data.get('klass')
    await message.answer(f'Для завершения регистрации проверь правильность введенных данных.\n'
                         f'Имя: {name}\n'
                         f'Фамилия: {last_name}\n'
                         f'Класс: {klass}',reply_markup=conf_kb)
    await state.set_state(StepsReg.CONFIRM)

async def reg_stop(message: Message, state: FSMContext, bot:Bot):
    if message.text=='ОК':
        await message.answer(f'Регистрация завершена успешно.')
        await message.answer('Сохраняю ваши данные...')
        client_data = await state.get_data()
        db = DataBase('utils/database.db')
        db.add_client(message.from_user.id,client_data.get('name'),client_data.get('last_name'),client_data.get('klass'))
        await message.answer('Ваши данные сохранены.')
        await bot.send_message(settings.bots.admin_id, text='Подана новая заявка на регистрацию.')
    else:
        await message.answer(f'Регистрация отменена.')
    await state.clear()


def register_reg_client(dp: Dispatcher):
    dp.message.register(reg_start, F.text=='регистрация')
    dp.message.register(get_name, StepsReg.GET_NAME)
    dp.message.register(get_klass, StepsReg.GET_LAST_NAME)
    dp.message.register(reg_confirm,StepsReg.GET_KLASS)
    dp.message.register(reg_stop,StepsReg.CONFIRM)
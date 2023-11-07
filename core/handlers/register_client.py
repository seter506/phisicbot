from aiogram import Dispatcher,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import StepsReg
from aiogram.filters import Command
from core.keyboards.reg_kb import klass_kb, conf_kb
from aiogram.types import ContentType


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

async def reg_stop(message: Message, state: FSMContext):
    if message.text=='ОК':
        await message.answer(f'Регистрация завершена успешно.')
        await message.answer('Сохраняю ваши данные...')
    else:
        await message.answer(f'Регистрация отменена.')
    await state.clear()


def register_reg_client(dp: Dispatcher):
    dp.message.register(reg_start, Command(commands=['reg']))
    dp.message.register(get_name, StepsReg.GET_NAME)
    dp.message.register(get_klass, StepsReg.GET_LAST_NAME)
    dp.message.register(reg_confirm,StepsReg.GET_KLASS)
    dp.message.register(reg_stop,StepsReg.CONFIRM)
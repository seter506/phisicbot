from aiogram import Dispatcher,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import StepsReg
from aiogram.filters import Command
from aiogram.types import ContentType


async def reg_start(message:Message,state:FSMContext):
    await message.answer(f'Начинаем регистрацию. Введите свое имя.')
    await state.set_state(StepsReg.GET_NAME)


def register_reg_client(dp: Dispatcher):
    dp.message.register(reg_start, Command(commands=['reg']))
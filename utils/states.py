from aiogram.fsm.state import StatesGroup, State


class StepsReg(StatesGroup):
    GET_NAME = State()
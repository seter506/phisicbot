from aiogram.fsm.state import StatesGroup, State


class StepsReg(StatesGroup):
    GET_NAME = State()
    GET_SECOND_NAME = State()
    GET_KLASS = State()
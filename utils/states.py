from aiogram.fsm.state import StatesGroup, State


class StepsReg(StatesGroup):
    GET_NAME = State()
    GET_LAST_NAME = State()
    GET_KLASS = State()
    CONFIRM = State()

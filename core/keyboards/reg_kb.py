from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from core.settings import klass

reg_kb=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/reg')]],resize_keyboard=True,one_time_keyboard=True)

conf_kb=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ОК')],[KeyboardButton(text='Отмена')]],
                            resize_keyboard=True,one_time_keyboard=True)

def klass_kb():
    keyboard_builder=ReplyKeyboardBuilder()
    for butt in klass:
        keyboard_builder.button(text=butt)
    # keyboard_builder.button(text='7б')
    # keyboard_builder.button(text='7в')
    # keyboard_builder.button(text='7г')
    # keyboard_builder.button(text='7д')
    # keyboard_builder.button(text='7е')
    # keyboard_builder.button(text='8а')
    # keyboard_builder.button(text='8б')
    # keyboard_builder.button(text='8в')
    # keyboard_builder.button(text='8г')
    # keyboard_builder.button(text='8д')
    # keyboard_builder.button(text='8м')
    # keyboard_builder.button(text='9б')
    # keyboard_builder.button(text='9в')
    # keyboard_builder.button(text='9г')
    # keyboard_builder.button(text='9д')
    keyboard_builder.adjust(6,6,4)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
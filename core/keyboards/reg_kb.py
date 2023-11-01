from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

reg_kb=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Регистрация')]],resize_keyboard=True,one_time_keyboard=True)

# def get_reg_kb():
#     keyboard_builder=ReplyKeyboardBuilder()
#     keyboard_builder.button(text='Регистрация')
#     return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
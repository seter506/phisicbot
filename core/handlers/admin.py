from aiogram import Dispatcher,F
from aiogram.types import Message, InlineKeyboardButton,InlineKeyboardMarkup
from core.keyboards.admin_kb import admin_menu_kb
from aiogram.filters import Command
from utils.db_class import DataBase
from core.handlers.callback import client_confirm

async def get_adm_menu(message: Message):
    await message.answer(f'Вывожу меню.', reply_markup=admin_menu_kb)

async def get_unconf_clients(message: Message):
    db = DataBase('utils/database.db')
    cl=db.get_unconf_clients()
    await message.answer(f'Вывожу список.')
    await message.answer('*** НАЧАЛО СПИСКА ***')
    for i in cl:
        inl_ok = InlineKeyboardButton(text='Подтвердить', callback_data=f'conf_ok_{i[0]}_{i[4]}')
        inl_can = InlineKeyboardButton(text='Отменить', callback_data=f'conf_cancel_{i[0]}_{i[4]}')
        inl_kb = InlineKeyboardMarkup(inline_keyboard=[[inl_ok,inl_can]])
        await message.answer(
            f'Ученик №{i[0]}.\nИмя: {i[1]}\nФамилия: {i[2]}\nКласс: {i[3]}', reply_markup=inl_kb)
    await message.answer(f'*** КОНЕЦ СПИСКА ***')
    print(cl)


def register_admin(dp: Dispatcher):
    dp.message.register(get_adm_menu, Command(commands=['admin_menu']))
    dp.message.register(get_unconf_clients, F.text=='заявки')
    dp.callback_query.register(client_confirm, F.data.startswith('conf_'))
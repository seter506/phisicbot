from aiogram import Bot
from aiogram.types import CallbackQuery

async def client_confirm(call: CallbackQuery, bot: Bot):
    conf=call.data.split('_')[1]
    client=call.data.split('_')[2]
    answer=f'Была нажата кнопка с параметрами: {conf} - {client}'
    await call.answer(answer)
    await call.answer()


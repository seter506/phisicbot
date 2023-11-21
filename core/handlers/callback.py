from aiogram import Bot
from aiogram.types import CallbackQuery
from utils.db_class import DataBase

async def client_confirm(call: CallbackQuery, bot: Bot):
    conf=call.data.split('_')[1]
    client=call.data.split('_')[2]
    id_tel=call.data.split('_')[3]
    print(conf,client,id_tel)
    db=DataBase('utils/database.db')
    if conf=='ok':
        db.conf_ok_client(id_tel)
        await call.answer(f'Ученик под номером {client} подтвержден.')
        await bot.send_message(id_tel,text='Ваша заявка подтверждена.')
    else:
        db.cursor.execute('DELETE FROM clients WHERE id_tel=?',(id_tel,))
        await call.answer(f'Заявка ученика {client} отклонена.')
        await bot.send_message(id_tel,text='Ваша заявка отклонена. Попробуйте еще раз.')


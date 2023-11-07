from aiogram import Bot, Dispatcher
import asyncio
import logging
import sqlite3
from core.handlers.basic import register_basic_handlers
from core.handlers.register_client import register_reg_client
from core.settings import settings
from utils.db_class import DataBase



async def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(name)s - '
                                                   '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    register_basic_handlers(dp)
    register_reg_client(dp)
    db=DataBase('utils/database.db')
    db.create_table()

    try:

        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == "__main__":
    asyncio.run(start())
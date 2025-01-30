import asyncio
import logging
from aiogram import Bot

from bot_config import bot,dp,database
from handlers.start import start_router
from handlers.homework import homework_router

async def startup(bot: Bot):
    database.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(homework_router)
    dp.startup.register(startup)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
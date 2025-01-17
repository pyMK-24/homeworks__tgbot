import asyncio
import logging
from  aiogram import Bot

from bot_config import bot,dp,database
from handlers.start import start_router   
from handlers.other_commands import other_router
from handlers.dialog_rewiew import dialog_review

async def on_startup(bot: Bot):
    database.create_table()

async def main():
    dp.include_router(start_router)
    dp.include_router(dialog_review)
    dp.include_router(other_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
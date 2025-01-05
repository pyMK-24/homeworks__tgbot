import asyncio
import random
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

names_list = ["Хауди Хо","John","Oleg","Alex","Arthur","Maxim","Tyler","Ivan"]

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")
    
@dp.message(Command("myinfo"))
async def get_info_handler(message: types.Message):
    id = message.from_user.id 
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(str((f"Твой id: {id}")))
    await message.answer(f"Твое имя: {first_name}")
    await message.answer(f"Твой никнейм: {username}")
    


@dp.message(Command("random"))
async def random_m_handler(message: types.Message):
    random_name = random.choice(names_list)
    await message.answer(f"Твое случайное имя: {random_name}")
    
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
from aiogram import Router,types
from aiogram.filters import Command 

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu_handler(message: types.Message):
    await message.answer("""Вот наше меню:
Мясная с аджикой 30cm
Баварская 30cm
Сырная 30cm
Ветчина и сыр 30 cm
Двойной цыпленок 30cm
Маргарита 30cm
Песто 30cm
Карбонара 30cm
Аррива! 30cm""")

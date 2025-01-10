from aiogram import Router,types
from aiogram.filters import Command 

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu_handler(message: types.Message):
    await message.answer("""Вот наше меню:
Мясная с аджикой 30cm, /pic_myasnay 
Баварская 30cm, /pic_bavarskay
Сырная 30cm, /pic_sirnay
Ветчина и сыр 30 cm, /pic_vetchina_sir
Двойной цыпленок 30cm, /pic_dvoinoi_ciplenok
Маргарита 30cm, /pic_margarita
Песто 30cm, /pic_pesto
Карбонара 30cm, /pic_karbonara
Аррива! 30cm, /pic_arriva """)

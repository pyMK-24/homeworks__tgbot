from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database

catalog_dishes_router = Router()

@catalog_dishes_router.message(Command("alldishes"))
async def all_dishes(message: types.Message):
    dishes_list = database.get_all_dishes()
    for dish in dishes_list:
        await message.answer(f"Название: {dish.get('name')}"
            f"\nЦена: {dish.get('price')} "
            f"\nОписание: {dish.get('description')} "
            f"\nКатегория: {dish.get('category')} "
            f"\nВариант порции блюда: {dish.get('option')}")
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot_config import database
from database import Database

dishes_admin_router = Router()
dishes_admin_router.message.filter(F.from_user.id == 7277047151)

class Dishes(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()
    option = State()
    
@dishes_admin_router.message(Command("dishes"))
async def new_dish(message: types.Message, state: FSMContext):
    await message.answer("Введите названия блюда")
    message.from_user.id
    await state.set_state(Dishes.name)
    
@dishes_admin_router.message(Dishes.name)
async def dish_name(message: types.Message, state: FSMContext):
    await message.answer("Введите цену блюда")
    await state.update_data(name=message.text)
    await state.set_state(Dishes.price)
    
@dishes_admin_router.message(Dishes.price)
async def dish_name(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer("Введите только цифры")
        return    
    price = int(price)
    if price < 0 or price > 5000:
        await message.answer("Введите цену не меньше 0 и не больше 5000")
        return
    await state.update_data(price=message.text)
    await message.answer("Введите описание блюда")
    await state.set_state(Dishes.description)
    
@dishes_admin_router.message(Dishes.description)
async def dish_name(message: types.Message, state: FSMContext):
    await message.answer("Введите категорию блюда")
    await state.update_data(description=message.text)
    await state.set_state(Dishes.category)
    
@dishes_admin_router.message(Dishes.category)
async def dish_name(message: types.Message, state: FSMContext):
    await message.answer("Введите вариант порции блюда")
    await state.update_data(category=message.text)
    await state.set_state(Dishes.option)
    
@dishes_admin_router.message(Dishes.option)
async def dish_name(message: types.Message, state: FSMContext):
    await message.answer("Данное  блюдо теперь у нас сохранено.")
    await state.update_data(option=message.text)
    data = await state.get_data()
    database.save_dish(data)
    await state.clear()    

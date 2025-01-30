from aiogram import Router,types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state

from bot_config import database

homework_router = Router()

class Homework(StatesGroup):
    name = State()
    number = State()
    link = State()
    
@homework_router.message(Command("stop"))
async def stop_dialog(message: types.Message, state: FSMContext):
    await message.answer("Диалог остановлен")
    await state.clear()

@homework_router.message(Command("homework"),default_state)
async def start_homework(message: types.Message, state: FSMContext):
    await message.answer("Оставьте тут свою домашку используя диалог, или можно его оставить с помощью команды /stop.")
    await message.answer("Как Вас зовут?")
    await state.set_state(Homework.name)
    
@homework_router.message(Homework.name)
async def procces_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=message.text)
    await message.answer("Введите номер вашего ДЗ")
    await state.set_state(Homework.number)
    
@homework_router.message(Homework.number)
async def procces_number(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data(number=number)
    await message.answer("Оставьте ссылку вашей работы")
    await state.set_state(Homework.link)
    
@homework_router.message(Homework.link)
async def procces_link(message: types.Message, state: FSMContext):
    link = message.text
    await state.update_data(link=link)
    await message.answer("Ваша работа сохранена.")
    data = await state.get_data()
    database.save_homework(data)
    await state.clear()
    
    

from aiogram import Router,types
# from aiogram.filters import Command 

other_router =  Router()

@other_router.message()
async def echo_handler(message: types.message):
    await message.answer("Прошу прощение,используйте только команды или кнопки.")
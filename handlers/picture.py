from aiogram import Router,types
from aiogram.filters import Command 

picture_router = Router()

@picture_router.message(Command("pic_myasnay"))
async def send_photo_handler(message: types.Message):
    photo_maysnay = types.FSInputFile("images/mysnay.png")
    await message.answer_photo(photo = photo_maysnay,caption="Мясная с аджикой")
    
@picture_router.message(Command("pic_bavarskay"))
async def send_photo_handler(message: types.Message):
    photo_bavarskay = types.FSInputFile("images/bavarskay.png")
    await message.answer_photo(photo = photo_bavarskay,caption="Баварская")

@picture_router.message(Command("pic_sirnay"))
async def send_photo_handler(message: types.Message):
    photo_sirnay = types.FSInputFile("images/sirnay.png")
    await message.answer_photo(photo = photo_sirnay,caption="Сырная")
    
@picture_router.message(Command("pic_vetchina_sir"))
async def send_photo_handler(message: types.Message):
    photo_vetchina_sir = types.FSInputFile("images/vetchina_sir.png")
    await message.answer_photo(photo = photo_vetchina_sir,caption="Ветчина и сыр")
    
@picture_router.message(Command("pic_dvoinoi_ciplenok"))
async def send_photo_handler(message: types.Message):
    photo_dvoinoi_ciplenok = types.FSInputFile("images/dvoinoi_ciplenok.png")
    await message.answer_photo(photo = photo_dvoinoi_ciplenok,caption="Двойной цыпленок")
    
@picture_router.message(Command("pic_margarita"))
async def send_photo_handler(message: types.Message):
    photo_margarita = types.FSInputFile("images/margarita.png")
    await message.answer_photo(photo = photo_margarita,caption="Маргарита")
    
@picture_router.message(Command("pic_pesto"))
async def send_photo_handler(message: types.Message):
    photo_pesto = types.FSInputFile("images/pesto.png")
    await message.answer_photo(photo = photo_pesto,caption="Песто")
    
@picture_router.message(Command("pic_karbonara"))
async def send_photo_handler(message: types.Message):
    photo_karbonara = types.FSInputFile("images/karbonara.png")
    await message.answer_photo(photo = photo_karbonara,caption="Карбонара")
    
@picture_router.message(Command("pic_arriva"))
async def send_photo_handler(message: types.Message):
    photo_arriva = types.FSInputFile("images/arriva.png")
    await message.answer_photo(photo = photo_arriva,caption="Аррива")
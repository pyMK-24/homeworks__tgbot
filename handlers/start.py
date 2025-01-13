from aiogram import types,F,Router
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Каталог блюд",callback_data="catalog")  
        ],
        [
            types.InlineKeyboardButton(text="Наш сайт",url="https://www.gastronome-restaurant.com")
        ],
        [
            types.InlineKeyboardButton(text="Связь с нами",callback_data="phone_nums")
        ],
        [
            types.InlineKeyboardButton(text="О нас",callback_data="about_us")
        ],
        [
            types.InlineKeyboardButton(text="Наш инстаграм",url="https://www.instagram.com/restaurant_gastronome"),
            types.InlineKeyboardButton(text="Наш ютуб",url="https://www.youtube.com/c/RestoranGastronome")
        ],
        [
            types.InlineKeyboardButton(text="Оставить отзыв",callback_data="review")
        ]
        ]
    )
    await message.answer(f"Здравствуйте, {name}.Это ресторан Gastronome.",reply_markup=keyboard)
    
@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.message.answer("""Мы — ресторан, где каждое блюдо — это настоящее искусство.
                                    \nМы готовим изысканные блюда с любовью и только из самых свежих ингредиентов.
                                    \nВ нашем меню ты найдешь как классические кулинарные шедевры, так и уникальные сочетания вкусов, которые приятно удивят.
                                    \nМы создаем атмосферу уюта и наслаждения, а обслуживание всегда на высшем уровне.
                                    \nПриходи, наслаждайся вкусом и открывай для себя новые гастрономические горизонты!""")

@start_router.callback_query(F.data == "phone_nums")
async def phone_nums_handler(callback: types.CallbackQuery):
    await callback.message.answer("Наши номера: \n+7 (495) 123-45-67 \n+7 (800) 765-43-21")
    
@start_router.callback_query(F.data == "catalog")
async def catalog_handler(callback: types.CallbackQuery):
    menu = """
    Закуски: 
        1. Цезарь с курицей - 450 руб
        2. Тартар из лосося - 550 руб
        3. Брускетты с помидорами и базиликом - 250 руб
    Основные блюда: 
        1. Стейк Рибай с овощами гриль - 1200 руб
        2. Ризотто с грибами - 650 руб
        3. Курица на гриле с картофельным пюре - 750 руб
    Десерты: 
        1. Тирамису - 350 руб
        2. Шоколадный фондан - 400 руб
        3. Панна котта с ягодами - 300 руб
    Напитки: 
        1. Свежевыжатый апельсиновый сок - 250 руб
        2. Домашний лимонад - 220 руб
        3. Минеральная вода (без газа) - 100 руб
    """
    await callback.message.answer(menu)
    


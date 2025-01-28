from aiogram import types,F,Router
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Каталог блюд с пагинацией",callback_data="alldishes")  
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

    


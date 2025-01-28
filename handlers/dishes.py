from aiogram import Router, F, types
from bot_config import database
from aiogram_widgets.pagination import TextPaginator
from bot_config import database

catalog_dishes_router = Router()

@catalog_dishes_router.callback_query(F.data == "alldishes")
async def all_dishes(callback: types.CallbackQuery):
    await callback.message.answer("Наш каталог блюд: ")
    dishes_list = database.get_all_dishes()
    dish_data = [f"Название: {dish.get('name')}"
            f"\nЦена: {dish.get('price')} "
            f"\nОписание: {dish.get('description')} "
            f"\nКатегория: {dish.get('category')} "
            for dish in dishes_list]
    
    paginator = TextPaginator(data=dish_data,router=catalog_dishes_router,per_page=1)
    current_text_chunk, reply_markup = paginator.current_message_data

    await callback.message.answer(
        text=current_text_chunk, 
        reply_markup=reply_markup
    )
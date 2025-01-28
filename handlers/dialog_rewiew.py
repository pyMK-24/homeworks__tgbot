from aiogram import types,F,Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup,default_state
from bot_config import database

dialog_review = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()    

@dialog_review.message(Command("stop"))
@dialog_review.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    await message.answer("Диалог прерван.")
    await state.clear()
 
@dialog_review.callback_query(F.data == "review",default_state)
async def review_name_handler(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.message.answer("Оставьте жалобу ответив на несколько вопросов. Можете остановить диалог с ботом введя '/stop' или 'стоп'")
    await callback_query.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)
    
@dialog_review.message(RestourantReview.name)
async def review_phone_number_handler(message: types.Message, state: FSMContext):
    name =  message.text
    await state.update_data(name = message.text) 
    await message.answer("Ваш номер телефона?")
    await state.set_state(RestourantReview.phone_number)

@dialog_review.message(RestourantReview.phone_number)
async def review_rate_handler(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Какую оценку поставите нашему ресторану?От 1 до 5.")
    await state.set_state(RestourantReview.rate)
    
@dialog_review.message(RestourantReview.rate)
async def review_extra_comments_handler(message: types.Message, state: FSMContext):
    rate = message.text
    if not rate.isdigit():
        await message.answer("Вводите только цифры.")
        return
    rate = int(rate)
    if rate < 1 or rate > 5:
        await message.answer("Вводите только от 1 до 5")
        return
    await state.update_data(rate = rate)
    await message.answer("Напишите пожалуйста отзыв про наш ресторан.")
    await state.set_state(RestourantReview.extra_comments)
    
@dialog_review.message(RestourantReview.extra_comments)
async def review_extra_com_handler(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    await message.answer("Спасибо за Ваш отзыв!")
    data = await state.get_data()
    database.save_review(data)
    await state.clear()

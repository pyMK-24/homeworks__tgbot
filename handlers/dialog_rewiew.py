from aiogram import types,F,Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

dialog_review = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()    

   
@dialog_review.callback_query(F.data == "review")
async def review_name_handler(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)
    
@dialog_review.message(RestourantReview.name)
async def review_phone_number_handler(message: types.Message, state: FSMContext):
    await message.answer("Ваш номер телефона?")
    await state.set_state(RestourantReview.phone_number)

@dialog_review.message(RestourantReview.phone_number)
async def review_rate_handler(message: types.Message, state: FSMContext):
    await message.answer("Какую оценку поставите нашему ресторану?От 1 до 5.")
    await state.set_state(RestourantReview.rate)
    
@dialog_review.message(RestourantReview.rate)
async def review_extra_comments_handler(message: types.Message, state: FSMContext):
    await message.answer("Напишите пожалуйста отзыв про наш ресторан.")
    await state.set_state(RestourantReview.extra_comments)
    
@dialog_review.message(RestourantReview.extra_comments)
async def review_extra_com_handler(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за Ваш отзыв!")
    await state.set_state(RestourantReview.extra_comments)
    await state.clear()

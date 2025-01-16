from aiogram import Bot,Dispatcher
from dotenv import dotenv_values
from datebase import Datebase

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
datebase = Datebase("reviews.db")
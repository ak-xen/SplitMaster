from aiogram import Bot
import security
from potisepents import admin_id
from dotenv import dotenv_values

TOKEN = dotenv_values('.env')["TOKEN"]
bot = Bot(token=TOKEN)


async def on_startup():
    await bot.send_message(admin_id, 'Bot start!!!')

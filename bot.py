from aiogram import Bot
import security
from potisepents import admin_id

TOKEN = security.Token
bot = Bot(token=TOKEN)


async def on_startup():
    await bot.send_message(admin_id, 'Bot start!!!')

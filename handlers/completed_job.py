from datetime import datetime, timedelta

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from data.DBconnect import add_task, get_telephone_number
from bot import bot

router = Router()


@router.callback_query(F.data.startswith('completed_'))
async def took_task(callback: types.CallbackQuery):
    data = callback.data.split('_')
    id_task, user_id = data[1], data[2]

from aiogram import Router
from aiogram.filters import Command, CommandObject
from data.MasterDB import MasterDB
from filters.IsAdmin import IsAdmin
from aiogram.types import Message
router = Router()


@router.message(IsAdmin(), Command("del"))
async def del_master(message: Message, command: CommandObject):
    if command.args:
        id = command.args
        await MasterDB.del_master(id.strip())
        await message.answer(f'ID: {id} быд удален из базы!')
    else:
        await message.answer('Введите после команды /del_id id!')

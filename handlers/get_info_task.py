from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from data.TaskDB import TaskDB

router = Router()
td = TaskDB()


@router.message(Command("inf"))
async def info_task(message: Message, command: CommandObject):
    if command.args:
        id = command.args
        task, address, telephone, time_completed = await td.get_task_info(id)
        task_message = f"Задача: {task}\n" \
                       f"Адрес: {address}\n"\
                       f"Номер заказчика: {telephone}\n"
        await message.answer(task_message)
    else:
        await message.answer('<b>Введите после команды /del_id id!</b>')

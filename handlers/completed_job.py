from aiogram import Router, types
from data import TaskDB
from bot import bot
from data.MasterDB import MasterDB
from keyboards.complet_task import CallbackCompleteTask
from potisepents import admin

router = Router()
ms = MasterDB()


@router.callback_query(CallbackCompleteTask.filter())
async def completed(callback: types.CallbackQuery, callback_data: CallbackCompleteTask):
    await callback.message.edit_reply_markup()
    id_task = callback_data.id_task
    user_id = callback_data.user_id
    await TaskDB.TaskDB.completed_task(id_task, user_id)
    task, address, telephone, master, time_completed = await TaskDB.TaskDB.get_task_info(id_task)
    name, family = await ms.get_master_name(user_id)
    message = f"Задание выполнено!!!!!\n" \
              f"Мастер: {name} {family}\n" \
              f"Задача: {task}\n" \
              f"Адрес: {address}\n" \
              f"Номер заказчика: {telephone}\n" \
              f"Когда выполнено: {time_completed}\n"
    await bot.send_message(admin, message)

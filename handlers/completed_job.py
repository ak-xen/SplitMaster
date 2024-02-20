from aiogram import Router, types
from data import TaskDB
from bot import bot
from keyboards.complet_task import CallbackCompleteTask
from potisepents import admin_id

router = Router()


@router.callback_query(CallbackCompleteTask.filter())
async def completed(callback: types.CallbackQuery, callback_data: CallbackCompleteTask):
    await callback.message.edit_reply_markup()
    id_task = callback_data.id_task
    user_id = callback_data.user_id
    await TaskDB.TaskDB.completed_task(id_task, user_id)
    task, address, telephone, time_completed = await TaskDB.TaskDB.get_task_info(id_task)
    message = f"Задание выполнено!!!!!\n" \
              f"Задача: {task}\n" \
              f"Адрес: {address}\n" \
              f"Номер заказчика: {telephone}\n" \
              f"Когда выполнено: {time_completed}\n"
    await bot.send_message(admin_id, message)




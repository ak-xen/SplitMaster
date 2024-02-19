from aiogram import types, F, Router


from data.TaskDB import TaskDB
from keyboards import complet_task
from potisepents import channel_id
from bot import bot


new_task = TaskDB()
router = Router()


@router.callback_query(F.data.startswith('take_'))
async def took_task(callback: types.CallbackQuery):
    id_task = callback.data[5:]
    await callback.message.edit_reply_markup()
    user_id = callback.from_user.id
    await bot.forward_message(user_id, channel_id, callback.message.message_id)
    telephone_number = await new_task.get_telephone_number(id_task)
    await new_task.add_id_master_in_taskdb(id_task, user_id)
    await bot.send_message(user_id, f'Задание получено!\nНомер заказчика: {telephone_number}',
                           reply_markup=complet_task.completed_task(id_task, user_id).as_markup())

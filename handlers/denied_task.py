from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from data import TaskDB
from bot import bot
from data.MasterDB import MasterDB
from keyboards import give_task_kb
from keyboards.complet_task import CallbackDeniedTask
from potisepents import channel_id, admin

router = Router()
ms = MasterDB()
task = TaskDB.TaskDB()


class WhyDenied(StatesGroup):
    why_denied = State()


@router.callback_query(CallbackDeniedTask.filter())
async def denied(callback: types.CallbackQuery, callback_data: CallbackDeniedTask, state: FSMContext):
    await callback.message.edit_reply_markup()
    id_task = callback_data.id_task
    user_id = callback_data.user_id
    await task.set_id_master_in_taskdb(id_task, '')
    task_name, description, time, price, district = await task.get_info_task_for_message(id_task)
    task_message = f"Задача: {task_name}\n" \
                   f"Описание задачи:{description}\n" \
                   f"Время, когда нужно сделать: {time}\n" \
                   f"Цена: {price}\n" \
                   f"Район: {district}\n"
    await bot.send_message(chat_id=channel_id, text=task_message,
                           reply_markup=give_task_kb.take_task(id_task).as_markup())
    name, family = await ms.get_master_name(user_id)
    await bot.send_message(admin, f'Мастер: {name} {family}\nОтказался от задания №{id_task}')
    await state.set_state(WhyDenied.why_denied)
    await bot.send_message(chat_id=user_id, text='Напишите причину отказа!')


@router.message(WhyDenied.why_denied)
async def include_task(message: Message, state: FSMContext):
    cause = message.text
    await bot.send_message(admin, text=f'По причине: {cause}')
    await state.clear()

from datetime import datetime, timedelta

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.DBconnect import add_task, get_telephone_number, TaskDB, add_id_master_in_taskdb
from bot import bot
from potisepents import channel_id
from keyboards import give_task_kb, complet_task

router = Router()


class Task(StatesGroup):
    task = State()
    description = State()
    lead_time = State()
    address = State()
    price = State()
    telephone_number = State()


new_task = TaskDB()
delta = timedelta(hours=1)
time = datetime.now() + delta


@router.message(Command("task"))
async def create_task(message: Message, state: FSMContext):
    await message.answer(
        "Введите название задачи"
    )
    await state.set_state(Task.task)


@router.message(Task.task)
async def include_task(message: Message, state: FSMContext):
    new_task.task = message.text
    await message.answer("Введите описание задачи!")
    await state.set_state(Task.description)


@router.message(Task.description)
async def include_task(message: Message, state: FSMContext):
    new_task.description = message.text
    await message.answer("Введите когда нужно выполнить задание задание!")
    await state.set_state(Task.lead_time)


@router.message(Task.lead_time)
async def include_task(message: Message, state: FSMContext):
    new_task.lead_time = message.text
    await message.answer("Введите адресс на котором нужно выполнить задание!")
    await state.set_state(Task.address)


@router.message(Task.address)
async def include_task(message: Message, state: FSMContext):
    new_task.address = message.text
    await message.answer("Введите цену выполнения задания!")
    await state.set_state(Task.price)


@router.message(Task.price)
async def include_task(message: Message, state: FSMContext):
    new_task.price = message.text
    await message.answer("Введите телефонный номер заказчика!")
    await state.set_state(Task.telephone_number)


@router.message(Task.telephone_number)
async def include_task(message: Message, state: FSMContext):
    new_task.telephone_number = message.text
    new_task.status = 0
    new_task.time_created = time.strftime("%H:%M %d.%m.%Y")
    await message.answer("Задание зарегистрированно!!!")
    id_task = await add_task(new_task)
    await bot.send_message(channel_id, await create_message(), reply_markup=give_task_kb.take_task(id_task).as_markup())
    await state.clear()


async def create_message():
    task_message = f"Задача: {new_task.task}\n" \
                   f"Описание задачи:{new_task.description}\n" \
                   f"Время, когда нужно сделать: {new_task.lead_time}\n" \
                   f"Цена: {new_task.price}\n" \
                   f"Адрес: {new_task.address}\n"

    return task_message


@router.callback_query(F.data.startswith('take_'))
async def took_task(callback: types.CallbackQuery):
    id_task = callback.data[5:]
    await callback.message.edit_reply_markup()
    user_id = callback.from_user.id
    await bot.forward_message(user_id, channel_id, callback.message.message_id)
    telephone_number = await get_telephone_number(id_task)
    await add_id_master_in_taskdb(id_task, user_id)
    await bot.send_message(user_id, f'Задание получено!\nНомер заказчика: {telephone_number}',
                           reply_markup=complet_task.completed_task(id_task, user_id).as_markup())

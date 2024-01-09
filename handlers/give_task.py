from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.DBconnect import TaskDB, add_task

router = Router()


class Task(StatesGroup):
    task = State()
    description = State()
    lead_time = State()
    address = State()
    price = State()
    telephone_number = State()


record: dict = {}


@router.message(Command("task"))
async def create_task(message: Message, state: FSMContext):
    await message.answer(
        "Введите название задачи"
    )
    await state.set_state(Task.task)


@router.message(Task.task)
async def include_task(message: Message, state: FSMContext):
    task = message.text
    record['task'] = task
    await message.answer("Введите описание задачи!")
    await state.set_state(Task.description)


@router.message(Task.description)
async def include_task(message: Message, state: FSMContext):
    description = message.text
    record['description'] = description
    await message.answer("Введите когда нужно выполнить задание задание!")
    await state.set_state(Task.lead_time)


@router.message(Task.lead_time)
async def include_task(message: Message, state: FSMContext):
    lead_time = message.text
    record['lead_time'] = lead_time
    await message.answer("Введите адресс на котором нужно выполнить задание!")
    await state.set_state(Task.address)


@router.message(Task.address)
async def include_task(message: Message, state: FSMContext):
    address = message.text
    record['address'] = address
    await message.answer("Введите цену выполнения задания!")
    await state.set_state(Task.price)


@router.message(Task.price)
async def include_task(message: Message, state: FSMContext):
    price = message.text
    record['price'] = price
    await message.answer("Введите телефонный номер заказчика!")
    await state.set_state(Task.telephone_number)


@router.message(Task.telephone_number)
async def include_task(message: Message, state: FSMContext):
    telephone_number = message.text
    record['telephone_number'] = telephone_number
    await message.answer("Задание зарегистрированно!!!")
    record['is_took'] = 0
    record['time_created'] = '22222'
    await add_task(record)
    await state.clear()

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.MasterDB import MasterDB
from filters.IsAdmin import IsAdmin

router = Router()


class AddUser(StatesGroup):
    id = State()
    status = State()
    name = State()
    family = State()
    telephone_number = State()


new_user = MasterDB()


@router.message(IsAdmin(),Command("add"))
async def add_user(message: Message, state: FSMContext):
    await message.answer(
        "Введите id нового пользователя"
    )
    await state.set_state(AddUser.id)


@router.message(AddUser.id)
async def include_task(message: Message, state: FSMContext):
    new_user.id = message.text
    await message.answer("Если пользователь админ введите '1', если нет 'о'")
    await state.set_state(AddUser.status)


@router.message(AddUser.status)
async def include_task(message: Message, state: FSMContext):
    new_user.status = "admin" if message.text == "1" else ''
    await message.answer("Введите имя нового пользователя")
    await state.set_state(AddUser.name)


@router.message(AddUser.name)
async def include_task(message: Message, state: FSMContext):
    new_user.name = message.text
    await message.answer("Введите фамилию нового пользователя")
    await state.set_state(AddUser.family)


@router.message(AddUser.family)
async def include_task(message: Message, state: FSMContext):
    new_user.family = message.text
    await message.answer("Введите номер телефона пользователя!")
    await state.set_state(AddUser.telephone_number)


@router.message(AddUser.telephone_number)
async def include_task(message: Message, state: FSMContext):
    new_user.telephone_number = message.text
    await new_user.add_user()
    await message.answer("Пользователь зарегестрирован!!!")
    await state.clear()

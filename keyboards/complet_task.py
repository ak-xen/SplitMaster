from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


class CallbackCompleteTask(CallbackData, prefix="complet"):
    id_task: int
    user_id: int


def completed_task(id_task, user_id):
    builder = InlineKeyboardBuilder()
    callback_data = CallbackCompleteTask(id_task=id_task, user_id=user_id).pack()
    button_1 = InlineKeyboardButton(text='Задание выполнено!', callback_data=callback_data)
    builder.add(button_1)
    return builder

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


class CallbackCompleteTask(CallbackData, prefix="complet"):
    id_task: int
    user_id: int


class CallbackDeniedTask(CallbackData, prefix="denied"):
    id_task: int
    user_id: int


def completed_task(id_task, user_id):
    builder = InlineKeyboardBuilder()
    callback_data = CallbackCompleteTask(id_task=id_task, user_id=user_id).pack()
    callback_data_denied = CallbackDeniedTask(id_task=id_task, user_id=user_id).pack()
    button_1 = InlineKeyboardButton(text='Задание выполнено!', callback_data=callback_data)
    button_2 = InlineKeyboardButton(text='Отказаться!', callback_data=callback_data_denied)
    builder.add(button_1, button_2)
    return builder

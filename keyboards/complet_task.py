from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def completed_task(id_task, user_id):
    builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text='Задание выполнено!', callback_data=f'completed_{id_task}_{user_id}')
    builder.add(button_1)
    return builder

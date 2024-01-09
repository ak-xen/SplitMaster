from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def take_task(id):
    builder = InlineKeyboardBuilder()
    button_1 = InlineKeyboardButton(text='Взять заказ', callback_data=f'take_{id}')
    builder.add(button_1)
    return builder


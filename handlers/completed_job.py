from aiogram import Router, types, F
from aiogram.filters.callback_data import CallbackData

from keyboards.complet_task import CallbackCompleteTask
router = Router()


@router.callback_query(CallbackCompleteTask.filter())
async def took_task(callback: types.CallbackQuery, callback_data: CallbackCompleteTask):
    await callback.message.edit_reply_markup()



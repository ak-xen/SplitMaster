from aiogram import Router, types
from aiogram.filters import Command, CommandObject

router = Router()


@router.message(Command(commands=['backup']))
async def get_backup(message: types.Message):
    path = 'data/Db.db'
    file = types.FSInputFile(path)
    await message.answer('Ожидайте идет подготовка документа...')
    await message.answer_document(file)